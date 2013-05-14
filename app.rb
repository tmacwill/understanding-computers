require 'json'
require 'maruku'
require 'sinatra'
require 'yaml'

set :bind, '0.0.0.0'
set :port, 80

$chapters = {}
$toc = {}
$toc_list = ''
$base = File.expand_path(File.dirname(__FILE__))

##
# Build an HTML representation of the table of contents
#
def build_toc_list
    $toc_list = '<ul>'

    # load heading for each chapter
    $toc.each do |id, chapter|
        $toc_list += "<li><a href=\"/chapter/#{id}\">#{chapter['heading']}</a><ul>"

        # load all chapter subheadings
        chapter['subheadings'].each do |subheading|
            $toc_list += "<li><a href=\"/chapter/#{id}/#{subheading['id']}\">#{subheading['subheading']}</a></li>"
        end

        $toc_list += "</ul></li>"
    end

    $toc_list += '</ul>'
end

##
# Load the table of contents from yaml source
#
def load_toc
    # iterate over all chapters in yaml
    info = YAML.load_file($base + '/content/src/chapters.yaml')
    info.each_with_index do |chapter, i|
        # save all metadata from chapter
        id = chapter['id']
        $chapters[id] = { 'sequence' => i }
        chapter.each do |k, v|
            $chapters[id][k] = v
        end

        # create entry in the table of contents for the chapter
        $toc[id] = {
            'heading' => chapter['title'],
            'sequence' => i + 1,
            'subheadings' => []
        }
    end
end

##
# Load the chapters from markdown source
#
def load_chapters
    # laod each chapter
    $chapters.each do |id, chapter|
        content = IO.read($base + '/content/src/chapters/' + id + '.markdown')

        # parse contents to exact headings
        parsed = content.split("\n").map do |line|
            if line =~ /^##/
                subheading_id = line[3..-1].downcase.gsub(' ', '-')
                $toc[id]['subheadings'].push({
                    'id' => subheading_id,
                    'subheading' => line[3..-1]
                })

                line + ' {: #' + subheading_id + ' }'
            else
                line
            end
        end

        # compile markdown to html
        content = Maruku.new(parsed.join("\n")).to_html
        $chapters[id]['content'] = content
        puts "Loaded Chapter #{chapter['sequence'] + 1}..."
    end
end

# if json files already exist, then simply load them
if File.exists?($base + '/content/build/chapters.json') and
        File.exists?($base + '/content/build/toc.json')
    $chapters = JSON.parse(IO.read($base + '/content/build/chapters.json'))
    $toc = JSON.parse(IO.read($base + '/content/build/toc.json'))

# json files do not exist, so build from source
else
    # load table of contents and chapers from markdown source
    load_toc
    load_chapters

    # save to disk so we don't have to reload
    IO.write($base + '/content/build/chapters.json', $chapters.to_json)
    IO.write($base + '/content/build/toc.json', $toc.to_json)
end

build_toc_list

Dir['./models/*.rb', './controllers/*.rb'].each { |f| require f }
