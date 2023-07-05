#===============================================================================

import json

#===============================================================================

SCAN2PMR_FILE = 'sckan2pmr.json'

#===============================================================================

class SckanToPmr:
    def __init__(self) -> None:
        with open(SCAN2PMR_FILE, 'r') as f:
            self.__scan2pmr = json.load(f)

    def get_pmr_objects(self, term, obj_type):
        return self.__scan2pmr.get(term, {'exposure':[], 'workspace':[], 'cellml':[]})[obj_type]

#===============================================================================

import argparse
from tqdm import tqdm

#===============================================================================

def complete_fcannotation(source, destination, obj_type='exposure', min_sim=0.85):
    sckan2pmr = SckanToPmr()
    with open(source, 'r') as f:
        annotations = json.load(f)

    for ftu in tqdm(annotations['FTUs']):
        if 'Model' in ftu:
            objs = [obj for obj in sckan2pmr.get_pmr_objects(ftu['Model'], obj_type)
                    if obj[0] >= min_sim]
            if len(objs) > 0:
                ftu['PMR'] = objs

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

    args = parser.parse_args()
    complete_fcannotation(args.file, args.dest, args.objType, args.minSim)

if __name__ == '__main__':
    main()
    
#===============================================================================
