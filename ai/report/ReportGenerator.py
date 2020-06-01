from KMeansReportGenerator import KMeansReportGenerator

class ReportGenerator():

    def __init__(self, algorithm, data, training_result, map, col_names):
        self.algorithm = algorithm
        self.data = data
        self.col_names = col_names
        self.training_result = training_result
        self.map = map

    def generate(self):
        return getattr (self, "_report_" + self.algorithm.name) ()
        # try:
        #    return getattr(self, "_report_" + self.algorithm.name)()
        # except:
        #    print("Report for this algorithm is unavailable")
        # TODO:: catch errors

    def _report_kmeans(self):
        kmeans_generator = KMeansReportGenerator(self.data, self.training_result, self.map, self.col_names)
        return kmeans_generator.generate()

