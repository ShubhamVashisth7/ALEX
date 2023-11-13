import gdown

def download(datasets):
    for dataset, id in datasets.items():
        gdown.download(id=id, output=f'/data/learned-index/{dataset}.bin')

if __name__ == '__main__':
    download({'longitudes-200M': '1zc90sD6Pze8UM_XYDmNjzPLqmKly8jKl',
              'longlat-200M': '1mH-y_PcLQ6p8kgAz9SB7ME4KeYAfRfmR',
              'lognormal-190M': '1y-UBf8CuuFgAZkUg_2b_G8zh4iF_N-mq',
              'ycsb-200M': '1Q89-v4FJLEwIKL3YY3oCeOEs0VUuv5bD'})
    