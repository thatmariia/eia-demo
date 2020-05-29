import pandas as pd
from enum import Enum

class RawDataFetcher:

    def __init__(self, filename: str):
        self.filename = filename

    def fetch(self):
        fileformat = self._get_fileformat()
        try:
            return getattr(self, "_fetch_" + fileformat.name)()
        except:
            print("No fetcher for this format")

    def _get_fileformat(self):
        try:
            return SupportedDataFormats[self.filename.split(".")[-1]]
        except ValueError:
            print("This preprocessed_data format is not supported")

    def _fetch_csv(self):
        data = pd.read_csv(self.filename, index_col=False)

        assert len(data) > 0, "no rows found in preprocessed_data"
        assert len(data.describe()) > 0, "no columns found in preprocessed_data"

        return data

    def _fetch_xslx(self):
        pass

class SupportedDataFormats(Enum):
    csv = "csv"
    xslx = "xlsx"

def list_SupportedDataFormats():
    return [f.name for f in SupportedDataFormats]
