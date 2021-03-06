Hyperparameter Tuning Example
------------------------------

Example of how to do hyperparameter tuning with MLflow and some popular optimization libraries.

This example tries to optimize the RMSE metric of a Keras deep learning model on a wine quality
dataset. The Keras model is fitted by the ``train`` entry point and has two hyperparameters that we
try to optimize: ``learning-rate`` and ``momentum``. The input dataset is split into three parts: training,
validation, and test. The training dataset is used to fit the model and the validation dataset is used to
select the best hyperparameter values, and the test set is used to evaluate expected performance and
to verify that we did not overfit on the particular training and validation combination.

examples/hyperparam/MLproject has 4 targets:
  * train
    train simple deep learning model on the wine-quality dataset from our tutorial.
    It has 2 tunable hyperparameters: ``learning-rate`` and ``momentum``.
    Contains examples of how Keras callbacks can be used for MLflow integration.
  * random
    perform simple random search over the parameter space.
  * gpyopt
    use `GPyOpt <https://github.com/SheffieldML/GPyOpt>`_ to optimize hyperparameters of train.
    GPyOpt can run multiple mlflow runs in parallel if run with ``batch-size`` > 1 and ``max_p`` > 1.
  * hyperopt
    use `Hyperopt <https://github.com/hyperopt/hyperopt>`_ to optimize hyperparameters.