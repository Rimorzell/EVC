# Copyright TU Wien (2022) - EVC: Task3
# Computer Vision Lab
# Institute of Computer Graphics and Algorithms

import numpy as np


def rgb2gray(rgb: np.ndarray):
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return np.clip(gray, 0, 1)


def evc_compute_brightness(input_image: np.ndarray) -> np.ndarray:
    """
    Calculates the brightness of the input image. First the image is normalized
    by multiplying it with the reciprocal of the maximum value of all three
    color channels. The brightness is then retrieved by computing a gray-scale
    image. Afterwards, the result is multiplied by the maximum value.

    Args:
        input_image: Image matrix of dimension: (n, m, 3)

    Returns:
        The brightness of the image, matrix of dimension (n, m)
    """
    ### STUDENT CODE
    max_val = np.max(input_image)
    if max_val == 0:
        max_val = 1e-10
    normalized = input_image * (1.0 / max_val)
    brightness = rgb2gray(normalized) * max_val
    ### END STUDENT CODE

    return brightness


def evc_compute_chromaticity(
    input_image: np.ndarray, brightness: np.ndarray
) -> np.ndarray:
    """
    Calculates the chromaticity of the 'input' image using the 'brightness'
    values. Therefore, the color channels of the input image are individually
    divided by the brightness values.

    Args:
        input_image: Image matrix of dimension: (n, m, 3)
        brightness: Brightness values, matrix of dimension (n, m)

    Returns:
        The chromaticity of the image, dimension (n, m, 3)
    """
    ### STUDENT CODE
    safe_brightness = np.where(brightness == 0, 1.0, brightness)
    r = input_image[:, :, 0] / safe_brightness
    g = input_image[:, :, 1] / safe_brightness
    b = input_image[:, :, 2] / safe_brightness
    chromaticity = np.dstack([r, g, b])
    ### END STUDENT CODE

    return chromaticity


def evc_gamma_correct(input_image: np.ndarray, gamma: float) -> np.ndarray:
    """
    Performs gamma correction on the 'input_image' image. This is done by
    raising it to the power of the reciprocal value of gamma (gamma**(-1)).

    Args:
        input_image: The image.
        gamma: The gamma value.

    Returns:
        The image after gamma correction.
    """
    ### STUDENT CODE
    if gamma < 1e-10:
        gamma = 1e-10
    corrected = np.power(input_image, 1.0 / gamma)
    ### END STUDENT CODE

    return corrected


def evc_reconstruct(
    brightness_corrected: np.ndarray, chromaticity: np.ndarray
) -> np.ndarray:
    """
    Reconstructs the color values by multiplying the corrected brightness with
    the chromaticity.

    Args:
        brightness_corrected: Gamma-corrected brightness values.
        chromaticity: Chromaticity values.

    Returns:
        The reconstructed image.
    """
    ### STUDENT CODE
    r = chromaticity[:, :, 0] * brightness_corrected
    g = chromaticity[:, :, 1] * brightness_corrected
    b = chromaticity[:, :, 2] * brightness_corrected
    result = np.dstack([r, g, b])
    ### END STUDENT CODE

    return result
