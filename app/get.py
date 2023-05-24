import pybase64
import requests
import binascii
import os



def decode_base64(encoded):

    decoded = ''
    for encoding in ['utf-8', 'iso-8859-1']:
        try:
            decoded = pybase64.b64decode(encoded + b'=' * (-len(encoded) % 4)).decode(encoding)
            break
        except (UnicodeDecodeError, binascii.Error):
            pass
    return decoded


def generate_v2ray_configs(decoded_data):

    configs = []

    for config in decoded_data:
        configs.append(config)

    sorted_configs = sorted(configs)

    return sorted_configs


def decode_links(links):

    decoded_data = []

    for link in links:
        response = requests.get(link)
        encoded_bytes = response.content
        decoded_text = decode_base64(encoded_bytes)
        decoded_data.append(decoded_text)

    sorted_configs = generate_v2ray_configs(decoded_data)

    return sorted_configs


def decode_dir_links(dir_links):


    decoded_dir_links = []

    for link in dir_links:
        response = requests.get(link)
        decoded_text = response.text
        decoded_dir_links.append(decoded_text)

    return decoded_dir_links


def main():
    links = [
        'https://raw.githubusercontent.com/MrPooyaX/VpnsFucking/main/Shenzo.txt',
        'https://raw.githubusercontent.com/MrPooyaX/SansorchiFucker/main/data.txt',
        'https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/Long_term_subscription1',
        'https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/Long_term_subscription8',
        'https://raw.githubusercontent.com/freefq/free/master/v2'
    ]
    dir_links = [
        'https://raw.githubusercontent.com/IranianCypherpunks/sub/main/config',
        'https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/sub/sub_merge.txt',
        'https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list_raw.txt'
    ]

    decoded_links = decode_links(links)
    decoded_dir_links = decode_dir_links(dir_links)
    merged_configs = decoded_links + decoded_dir_links
    output_folder = os.path.abspath(os.path.join(os.getcwd(), '.'))

    # Delete existing output files
    filename = os.path.join(output_folder, f'All_Configs_Sub.txt')
    if os.path.exists(filename):
        os.remove(filename)
    
    # Write merged configs to output file
    output_file = os.path.join(output_folder, 'All_Configs_Sub.txt')
    with open(output_file, 'w') as f:
        for config in merged_configs:
            f.write(config + '\n')

    
if __name__ == "__main__":
    main()


ptt = os.path.abspath(os.path.join(os.getcwd(), '.'))
ss_file = os.path.join(ptt, 'ss.txt')


open(ss_file, "w").close()
ss = ""
file_path = r'./All_Configs_Sub.txt'
with open(file_path, 'r') as file:
    response = file.read()

for config in response.splitlines():
    if config.startswith("ss"):   
        open(ss_file, "a").write(config + "\n")     
  
