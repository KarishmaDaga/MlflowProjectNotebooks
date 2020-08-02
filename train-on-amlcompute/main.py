from azureml import core
from azureml.core import Workspace

import mlflow

workspace = Workspace.from_config()  
mlflow.set_tracking_uri(workspace.get_mlflow_tracking_uri())

submitted_run = mlflow.projects.run(uri=".", 
                                    parameters={'alpha':0.3},
                                    experiment_name = "mlflow-train-on-remote",
                                    backend = "azureml",
                                    backend_config = "./backend_config.json")
