from KMeansReportGenerator import KMeansReportGenerator

class ReportGenerator():

    def __init__(self, algorithm,
                 data, raw_data, filtered_indices,
                 training_result, col_names):
        self.algorithm = algorithm
        self.data = data
        self.raw_data = raw_data
        self.filtered_indices = filtered_indices
        self.col_names = col_names
        self.training_result = training_result

    def generate(self):
        return getattr (self, "_report_" + self.algorithm.name) ()
        # try:
        #    return getattr(self, "_report_" + self.algorithm.name)()
        # except:
        #    print("Report for this algorithm is unavailable")
        # TODO:: catch errors

    def _report_kmeans(self):
        kmeans_generator = KMeansReportGenerator(self.data, self.raw_data, self.filtered_indices, self.training_result, self.col_names)
        return kmeans_generator.generate()

