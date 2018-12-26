import glob
import os

import pytest

HOWTO_DIR = os.path.realpath(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'howtos'))


@pytest.mark.parametrize('howto', sorted([x.split('/')[-1] 
                                          for x in glob.glob(os.path.join(HOWTO_DIR, 'how_to_*.py'))]))
def test_howto(howto, mongo_host):
    exec(open(HOWTO_DIR + "/" + howto).read(), {'mongo_host': mongo_host})
