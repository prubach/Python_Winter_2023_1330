from knotprot_download import get_proteins, download_link, setup_download_dir


def run_download_seq(my_dir):
    prot_list = get_proteins()
    i = 0
    for p in prot_list:
        download_link(my_dir, p)
        i += 1
    print(f'Downloaded: {i}')


if __name__ == '__main__':
    setup_download_dir()
    run_download_seq('images')