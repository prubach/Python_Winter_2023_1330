from concurrent.futures import ProcessPoolExecutor
from functools import partial
from multiprocessing import Pool
from pathlib import Path

from knotprot_download import get_proteins, download_link, setup_download_dir, time_it, create_thumbnail


def run_download_seq(my_dir):
    prot_list = get_proteins()
    i = 0
    for p in prot_list:
        download_link(my_dir, p)
        i += 1
    print(f'Downloaded: {i}')


def run_download_multiprocessing(my_dir):
    prot_list = get_proteins()
    download_func = partial(download_link, my_dir)
    with Pool(12) as pool:
        pool.map(download_func, prot_list)


def run_thumbnails_seq():
    file_list = Path('images').iterdir()
    for image_path in file_list:
        create_thumbnail((256, 256), image_path)


def run_thumbnails_parallel():
    file_list = Path('images').iterdir()
    create_thumb = partial(create_thumbnail, (256, 256))
    with ProcessPoolExecutor(max_workers=8) as executor:
        executor.map(create_thumb, file_list)


if __name__ == '__main__':
    setup_download_dir()
    #time_it(run_download_seq, 'images')
    time_it(run_download_multiprocessing, 'images')
    #time_it(run_thumbnails_seq)
    time_it(run_thumbnails_parallel)