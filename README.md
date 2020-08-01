# MlflowProjectNotebooks
Python notebooks with ML and deep learning examples with Mlflow Projects and AzureML SDK

To get started, go to [Configuration](configuration.md) to setup your environment.

## Navigating the Notebooks
Once your environment is good to go, get started with some of the sample projects in this repo.
I recommend walking through the training notebooks to see how to add the AzureML integration for MLflow Projects:
1. [Train locally](train-on-local) using your local compute and conda environment or a pre-configured environment
2. Train your project on remote compute using [AML Compute](train-on-amlcompute) or [Remote VMs](train-on-remote-vm)

Then move onto using the following sample projects from Mlflow to test the integration on different models and flows.
- [fastai](./fastai) modifies a fastai classification example and trains a simple MNIST model.
- [flower classifier](./flower_classifier)
- [gluon](./gluon)
- [h2o](./h2o) uses MLflow train models for predicting wine quality using random forests
- [hyperparam](./hyperparam) shows how to do hyperparameter tuning with MLflow and some popular optimization libraries.
- [keras](./keras) modifies a Keras classification example
- [lightgbm](./lightgbm)
- [mlflow-example](./mlflow-example) as used in the training notebook examples
- [multistep_workflow](./multistep_workflow) is an end-to-end of a data ETL and ML training pipeline built as an MLflow project. The example shows how parts of the workflow can leverage from previously run steps.
- [prophet](./prophet)
- [pytorch](./pytorch) uses CNN on MNIST dataset for character recognition.
- [sklearn_elasticnet_wine_quality](./sklearn_elasticnet_wine) uses the Wine Quality dataset and Elastic Net to predict quality. 
- [sklearn_logisic_regression](./sklearn_logisic_regression)
- [tensorflow](./tensorflow) contains end-to-end one run examples from train to predict for both TensorFlow 1.X and 2.0.
- [xgboost](./xgboost)


