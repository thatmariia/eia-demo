from KMeansReportGenerator import KMeansReportGenerator

class ReportGenerator():

    def __init__(self, algorithm):
        self.algorithm = algorithm
        self.gathered_data = None

    def generate(self):
        return getattr (self, "_report_" + self.algorithm.name) ()
        # try:
        #    return getattr(self, "_report_" + self.algorithm.name)()
        # except:
        #    print("Report for this algorithm is unavailable")
        # TODO:: catch errors

    def _report_kmeans(self):
        kmeans_generator = KMeansReportGenerator(self.gathered_data)
        return kmeans_generator.generate()
