# License: BSD 3 clause
"""
This package provides a number of utilities to make it simpler to run
common scikit-learn experiments with pre-generated features.

:author: Dan Blanchard (dblanchard@ets.org)
:author: Michael Heilman (mheilman@ets.org)
:author: Nitin Madnani (nmadnani@ets.org)
:organization: ETS
"""

from __future__ import absolute_import, print_function, unicode_literals

from sklearn.metrics import fbeta_score, make_scorer, SCORERS
from .logutils import get_skll_logger
from .data import FeatureSet, Reader, Writer
from .experiments import run_configuration
from .learner import Learner
from .metrics import (kappa, kendall_tau, spearman, pearson,
                      f1_score_least_frequent)


__all__ = ['FeatureSet', 'Learner', 'Reader', 'kappa', 'kendall_tau',
           'spearman', 'pearson', 'f1_score_least_frequent',
           'get_skll_logger', 'run_configuration', 'Writer']

# Add our scorers to the sklearn dictionary here so that they will always be
# available if you import anything from skll
_scorers = {'f1_score_micro': make_scorer(fbeta_score, beta=1,
                                          average='micro'),
            'f1_score_macro': make_scorer(fbeta_score, beta=1,
                                          average='macro'),
            'f1_score_weighted': make_scorer(fbeta_score, beta=1,
                                             average='weighted'),
            'f1_score_least_frequent': make_scorer(f1_score_least_frequent),
            'pearson': make_scorer(pearson),
            'spearman': make_scorer(spearman),
            'kendall_tau': make_scorer(kendall_tau),
            'unweighted_kappa': make_scorer(kappa),
            'quadratic_weighted_kappa': make_scorer(kappa,
                                                    weights='quadratic'),
            'linear_weighted_kappa': make_scorer(kappa, weights='linear'),
            'qwk_off_by_one': make_scorer(kappa, weights='quadratic',
                                          allow_off_by_one=True),
            'lwk_off_by_one': make_scorer(kappa, weights='linear',
                                          allow_off_by_one=True),
            'uwk_off_by_one': make_scorer(kappa, allow_off_by_one=True)}

SCORERS.update(_scorers)
