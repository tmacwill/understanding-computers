import e1.loader as loader
import e1.settings as settings

class ChapterBadge:
    def __init__(self, id, reads, points):
        self.id = id
        self.reads = reads
        self.points = points

    def earned(self):
        """
        Whether or not the badge has been earned
        """

        return self.percentage() == 100

    def milestones(self):
        """
        Determine which milestones have been reached
        """

        # load metadata for badge
        toc = loader.toc()
        psets = loader.psets()
        metadata = loader.badges()[self.id]
        milestones = {}

        # iterate over each chapter required for the badge
        for chapter in metadata['chapters']:
            # pset milestone reached if all points have been earned
            milestone = {
                'chapter': True,
                'pset': self.points[chapter] == psets['points'][chapter]
            }

            # chapter milestone not reached if some section has not been read
            for section in toc[chapter]['sections']:
                if not chapter in self.reads or not section['id'] in self.reads[chapter]:
                    milestone['chapter'] = False
                    break

            # save milestone
            milestones[chapter] = milestone

        return milestones

    def percentage(self):
        """
        Calculate what percentage of the badge has been completed
        """

        # load metadata for badge
        toc = loader.toc()
        psets = loader.psets()
        metadata = loader.badges()[self.id]

        # iterate over each chapter required for the badge
        total = 0
        earned = 0
        for chapter in metadata['chapters']:
            # check which sections in the chapter have been read
            for section in toc[chapter]['sections']:
                if chapter in self.reads and section['id'] in self.reads[chapter]:
                    earned += settings.POINTS['section']
                total += settings.POINTS['section']

            # add on points for pset
            earned += self.points[chapter]
            total += psets['points'][chapter]

        return float(earned) / float(total) * 100
