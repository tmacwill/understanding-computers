# table of contents page
get '/contents' do
    erb :contents
end

# read a chapter
get '/chapter/:chapter/?:section?' do |id, section|
    # get chapter information
    @chapter = id
    @number = $chapters[id]['sequence'] + 1
    @title = $chapters[id]['title']
    @content = $chapters[id]['content']

    erb :chapter
end
