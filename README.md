# MlflowProjectNotebooks
Training [MLflow Projects](https://mlflow.org/docs/latest/projects.html) using [Azure Machine Learning SDK](https://docs.microsoft.com/en-us/python/api/overview/azure/ml/?view=azure-ml-py) and services. 

To get started, go to [Configuration](configuration.md) to setup your environment.

## Navigating the Notebooks
Once your environment is good to go, get started with some of the sample projects in this repo.
I recommend walking through the training notebooks to see how to add the AzureML integration for MLflow Projects:
1. [Train locally](train-on-local) using your local compute and conda environment or a pre-configured environment
2. Train your project on remote compute using [AML Compute](train-on-amlcompute) or [Remote VMs](train-on-remote-vm)

Then move onto using the following sample projects from Mlflow to test the integration on different models and flows. For projects without an MLproject file, ensure you already have project dependencies installed. If you'd like to train a project remotely, it must have an MLproject file.
- [fastai](examples/fastai) modifies a fastai classification example and trains a simple MNIST model.
- [flower classifier](examples/flower_classifier)
- [h2o](examples/h2o) uses MLflow train models for predicting wine quality using random forests
- [hyperparam](examples/hyperparam) shows how to do hyperparameter tuning with MLflow and some popular optimization libraries.
- [lightgbm](examples/lightgbm)
- [mlflow-example](examples/mlflow-example) as used in the training notebook examples
- [multistep_workflow](examples/multistep_workflow) is an end-to-end of a data ETL and ML training pipeline built as an MLflow project. The example shows how parts of the workflow can leverage from previously run steps.
- [prophet](examples/prophet)
- [pytorch](examples/pytorch) uses CNN on MNIST dataset for character recognition.
- [sklearn_elasticnet_wine](examples/sklearn_elasticnet_wine) uses the Wine Quality dataset and Elastic Net to predict quality. 
- [sklearn_logisic_regression](examples/sklearn_logisic_regression)
- [tensorflow](examples/tensorflow) contains end-to-end one run examples from train to predict for both TensorFlow 1.X and 2.0.
- [xgboost](examples/xgboost)


