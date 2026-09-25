"""U-TILISE network as an installable package: `utilise.utilise.UTILISE`.

Every other module here is a symlink to the unchanged upstream file in `lib/models/`, so the
package holds the network, its layers and `weight_init` only, without the training scripts'
dependencies (wandb, omegaconf, numba, ...), which stay in the `scripts` dependency group.
"""
