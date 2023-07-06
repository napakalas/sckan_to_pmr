#===============================================================================

PMRSEARCH_URL = 'http://130.216.217.220/api/search/{}?query={}&context={}&minsim={}&cweight={}'

#===============================================================================

import json
import requests
import argparse
from tqdm import tqdm
import logging

#===============================================================================

def complete_fcannotation(source, destination, obj_type='exposure', min_sim=0.85, c_weight=0.8):
    with open(source, 'r') as f:
        annotations = json.load(f)

    for ftu in tqdm(annotations['FTUs']):
        if 'Model' in ftu:
            try:
                url = PMRSEARCH_URL.format(obj_type, ftu['Model'], ftu.get('Organ',''), min_sim, c_weight)
                response = requests.get(url)
                objs = response.json()
                if len(objs) > 0:
                    ftu['PMR'] = objs
            except:
                logging.warning(f"Server down: {ftu['Model']}")

    with open(destination, 'w') as f:
        json.dump(annotations, f)

def main():
    parser = argparse.ArgumentParser(description='Searching PMR models based on SCKAN term')
    parser.add_argument('--file', dest='file',
                        help='path to an annotation file')
    parser.add_argument('--dest', dest='dest', required=True,
                        help='path to save new annotation file')
    parser.add_argument('--type', dest='objType', default='exposure',
                        help='the object type to search (exposure|workspace|cellml)')
    parser.add_argument('--min-sim', dest='minSim', type=float, default=0.85,
                        help='minimum similarity of models to be added to the annotation file, default=0.85')
    parser.add_argument('--c-weight', dest='cWeight', type=float, default=0.8,
                        help='the weight of context, default=0.8')

    args = parser.parse_args()
    complete_fcannotation(args.file, args.dest, args.objType, args.minSim, args.cWeight)

if __name__ == '__main__':
    main()
    
#===============================================================================
