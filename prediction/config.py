import dataclasses


@dataclasses.dataclass
class TrainerConfig:
    num_epochs: int = 5
    batch_size: int = 32
    learning_rate: float = 1e-3


@dataclasses.dataclass
class ClassifierConfig:
    hid_size: int = 512
    dropout: float = 0.2


@dataclasses.dataclass
class Config:
    dataset_path: str = '../data/dataset-0.0.2.de.strat.parquet'

    encoder: str = 'Twitter/twhin-bert-base'

    data_out_dir: str = './data'
    result_dir: str = './results'
    test_size: float = 0.2

    text_column: str = 'response'
    label_column: str = 'model'

    trainer_config: TrainerConfig = dataclasses.field(default_factory=TrainerConfig)
    classifier_config: ClassifierConfig = dataclasses.field(default_factory=ClassifierConfig)
