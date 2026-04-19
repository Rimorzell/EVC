# Copyright TU Wien (2022) - EVC: Task3
# Computer Vision Lab
# Institute of Computer Graphics and Algorithms

import numpy as np


def evc_white_balance(input_image: np.ndarray, white: np.ndarray) -> np.ndarray:
    """
    Performs white balancing manually.

    Args:
        input_image: Image.
        white: A color (as RGB vector) that should become the new white.

    Returns:
        The image after the white balance.
    """
    ### STUDENT CODE
    white_arr = np.asarray(white, dtype=float)
    safe_white = np.where(white_arr == 0, 1.0, white_arr)
    result = input_image / safe_white
    ### END STUDENT CODE

    result = np.minimum(result, 1)

    return result
