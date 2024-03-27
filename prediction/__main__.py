import pathlib

import pandas as pd
from cltrier_prosem import Pipeline

import config

if __name__ == '__main__':
    CFG = config.Config()

    raw: pd.DataFrame = pd.read_parquet(CFG.dataset_path)

    pathlib.Path(CFG.data_out_dir).mkdir(parents=True, exist_ok=True)
    pathlib.Path(CFG.result_dir).mkdir(parents=True, exist_ok=True)

    train_cut: int = int(len(raw) - len(raw) * CFG.test_size)

    raw[:train_cut].to_parquet(f'{CFG.data_out_dir}/train.parquet')
    raw[train_cut:].to_parquet(f'{CFG.data_out_dir}/test.parquet')

    Pipeline({
        'encoder': {
            'model': CFG.encoder,
        },
        'dataset': {
            'path': CFG.data_out_dir,
            'text_column': CFG.text_column,
            'label_column': CFG.label_column,
            'label_classes': list(raw['model'].unique()),
        },
        'classifier': {
            **CFG.classifier_config.__dict__
        },
        'pooler': {
            'form': 'cls',
            'span_columns': [''],
        },
        'trainer': {
            **CFG.trainer_config.__dict__,
            'export_path': CFG.result_dir,
        },
    })()