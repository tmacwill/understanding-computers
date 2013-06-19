import e1.loader as loader

class ChapterBadge:
    def __init__(self, id, reads, points):
        self.id = id
        self.reads = reads
        self.points = points

    def earned(self):
        return True
        return self.percentage() == 1.

    def percentage(self):
        # load metadata for badge
        toc = loader.toc()
        psets = loader.psets()
        metadata = loader.badges()[self.id]

        # iterate over each section required for the badge
        total = 0
        earned = 0
        for chapter in metadata['chapters']:
            # check which sections in the chapter have been read
            for section in toc[chapter]['subheadings']:
                if chapter in reads and section in reads[chapter]:
                    earned += settings.POINTS['section']
                total += settings.POINTS['section']

            # add on points for pset
            earned = points[chapter]
            total += psets[chapter]['points']

        return earned / total
