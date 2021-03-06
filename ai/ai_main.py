from rawdata.RawDataFetcher import RawDataFetcher
from preprocessing.DataPreprocessor import DataPreprocessor
from algorithms.AlgorithmsManager import AlgorithmsManager
from training.TrainingAgent import TrainingAgent
from report.ReportGenerator import ReportGenerator


def run():
    # get the raw dataset
    # TODO:: ask user for dataset
    data_fetcher = RawDataFetcher(filename="test_datasets/MallCustomers.csv")
    raw_data = data_fetcher.fetch()

    # get the algorithm
    algorithms_manager = AlgorithmsManager()
    algorithm = algorithms_manager.select()

    # preprocess based on algorithm
    data_preprocessor = DataPreprocessor(algorithm, raw_data)
    data, col_names, filtered_indices = data_preprocessor.preprocess()
    print(data)

    # train
    training_agent = TrainingAgent(algorithm, data)
    training_result = training_agent.train()

    # generate report
    report_generator = ReportGenerator(algorithm=algorithm,
                                       data=data, raw_data=raw_data, filtered_indices=filtered_indices,
                                       training_result=training_result, col_names=col_names)
    report_generator.generate()

run()