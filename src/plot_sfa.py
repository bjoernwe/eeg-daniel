from typing import List

import numpy as np
import pandas
import plotly.express as px

from pathlib import Path
from pandas import DataFrame
from sksfa import SFA


def main():

    df = read_csv()

    data = np.array(df.to_numpy()[:, :10], dtype="float")
    sfa = SFA(3)
    features = sfa.fit_transform(data)

    labels = [is_fruition(notation) for notation in df["notation"]]
    plot(data=features, labels=labels)


def plot(data: np.ndarray, labels: List[int]):
    size = np.array([18*l + 2 for l in labels])
    fig = px.scatter_3d(x=data[:, 0], y=data[:, 1], z=data[:, 2], color=labels, size=size, color_continuous_scale="Bluered")
    #fig.update_traces(marker_size=3)
    fig.show()


def is_fruition(notation: str) -> int:
    return 1 if notation.lower().find("fruition") != -1 else 0


def read_csv() -> DataFrame:
    data_path = Path(__file__).parent.parent.joinpath("data")
    file_path = data_path.joinpath("daniel_fruitions_tagged.csv")
    return pandas.read_csv(file_path, dtype="float", converters={"day": str, "notation": str})


if __name__ == '__main__':
    main()
