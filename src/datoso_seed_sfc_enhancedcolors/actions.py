"""Actions for the sfc enhanced colors seed."""
from datoso.configuration import logger
from datoso_seed_sfc_enhancedcolors.dats import SFCEnhancedColorsDat

actions = {
    '{dat_origin}': [
        {
            'action': 'LoadDatFile',
            '_class': SFCEnhancedColorsDat,
        },
        {
            'action': 'DeleteOld',
            'folder': '{dat_destination}',
        },
        {
            'action': 'Copy',
            'folder': '{dat_destination}',
        },
        {
            'action': 'SaveToDatabase',
        },
    ],
}

def get_actions() -> dict:
    """Get the actions dictionary."""
    logger.error('Deprecated, use datoso_seed_enhanced instead')
    return actions
