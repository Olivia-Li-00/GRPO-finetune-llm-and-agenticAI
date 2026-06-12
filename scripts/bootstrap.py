import numpy as np

def bootstrap_ci(correct_flags,
                 partial_flags,
                 format_flags,
                 n_boot=2000,
                 alpha=0.05,
                 seed=None):
    """
    Bootstrap confidence intervals for accuracy, partial accuracy, and format accuracy.

    Each input is a list of 0/1 indicators, one value per evaluation question.

    returns:
        dict with mean, lower, upper for each metric
    """

    flags = {
        "accuracy": np.asarray(correct_flags, dtype=float),
        "partial_accuracy": np.asarray(partial_flags, dtype=float),
        "format_accuracy": np.asarray(format_flags, dtype=float),
    }
    n = len(flags["accuracy"])
    rng = np.random.default_rng(seed)

    boot_means = {
        "accuracy": [],
        "partial_accuracy": [],
        "format_accuracy": [],
    }

    for _ in range(n_boot):
        idx = rng.choice(n, size=n, replace=True)

        for name, values in flags.items():
            boot_means[name].append(values[idx].mean())

    results = {}

    for name, values in flags.items():
        lower = np.percentile(boot_means[name], 100 * alpha / 2)
        upper = np.percentile(boot_means[name], 100 * (1 - alpha / 2))

        results[name] = {
            "mean": values.mean(),
            "lower": lower,
            "upper": upper,
        }

    return results