from bs4 import BeautifulSoup
import pandas as pd
import urllib.request
import os
import licorice


def _return_soup(path):

    source = urllib.request.urlopen(path).read()

    return BeautifulSoup(source, features="html.parser")


def _find_latest_version(df):

    latest_version = df["version"].max()

    print(
        "Latest version of poolq: {}".format(
            licorice.font_format(latest_version, ["BOLD", "CYAN"])
        )
    )

    return latest_version


def _download_poolq(out_path, poolq_http, latest):

    """"""

    tmp_out_path = "poolq.tmp.zip"

    executable = "wget -q -O {} '{}'".format(tmp_out_path, poolq_http)
    os.system(executable)

    os.system("unzip -q {}".format(tmp_out_path))  # unzip
    os.system("rm -r {}".format(tmp_out_path))  # remove temp zip
    os.system(
        "rm -r poolq-{}/test-data/".format(latest)
    )  # remove uneccesary components (i.e., test data)

    os.system("mv poolq-{} {}".format(latest, out_path))


def _find_available_poolq_versions(poolq_path, download_path):

    """"""

    soup = _return_soup(poolq_path)

    poolq_distributions = {}
    poolq_distributions["name"] = []
    poolq_distributions["version"] = []
    poolq_distributions["path"] = []

    for line in soup.findAll("a"):
        if line.text.startswith("poolq-") and "zip" in line.text:
            poolq_distributions["name"].append(line.text)
            version = line.text.replace(".zip", "").split("-")[-1]

            poolq_distributions["version"].append(version)
            poolq_distributions["path"].append(
                download_path + "&filename=poolq-{}.zip".format(version)
            )

    return pd.DataFrame.from_dict(poolq_distributions)


class _poolq_downloader:

    """"""

    def __init__(self):

        """"""

        self.poolq_path = (
            "https://portals.broadinstitute.org/gpp/public/dir?dirpath=poolq-downloads"
        )
        self.download_path = "https://portals.broadinstitute.org/gpp/public/dir/download?dirpath=poolq-downloads&filename=poolq-{}.zip"

    def fetch_available(self):
        """"""

        self.version_df = _find_available_poolq_versions(
            self.poolq_path, self.download_path
        )
        self.latest = _find_latest_version(self.version_df)

    def download(self, out_path="./"):

        """"""

        poolq_http = self.download_path.format(self.latest)
        _download_poolq(out_path, poolq_http, self.latest)
        
        
def _look_for_poolq(path):

    """Check if poolq exists. If not, download it."""
    
    _poolq_download_path = os.path.join(os.path.dirname(path), "_distribution/")

    get_pq = _poolq_downloader()
    get_pq.fetch_available()
    if os.path.exists(_poolq_download_path + "poolq-{}".format(get_pq.latest)):
        print("\nLatest installation of poolq: poolq-{} previously installed.".format(get_pq.latest))
    else:
        get_pq.download(_poolq_download_path)
