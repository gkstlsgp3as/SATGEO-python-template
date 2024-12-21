# -*- coding: utf-8 -*-
'''
@Time          : 2024/12/18 00:00
@Author        : Shinhye Han
@File          : evaluate.py
@Noice         : 
@Description   : Evaluate a XXX model.
@How to use    : python evaluate.py -i {input_dir} -m {meta_file} -p {model_path} -c {classes}

@Modificattion :
    @Author    :
    @Time      :
    @Detail    :
'''

import argparse
from torch.utils.data import DataLoader
from utils.datasets import Dataset
from models.model_selector import create_model
import torch


def evaluate_model(data_dir, meta_file, model_path, device, config):
    """
    Evaluate the model on the validation dataset.

    Args:
        data_dir (str): Path to the validation dataset.
        meta_file (str): Path to the metadata file.
        model_path (str): Path to the trained model.
        device (torch.device): Device to use for evaluation.
        config (dict): Configuration dictionary with evaluation parameters.

    Returns:
        dict: Evaluation metrics (e.g., accuracy).
    """
    # Dataset and DataLoader
    dataset = Dataset(data_dir, classes=config["classes"], transforms=None)
    data_loader = DataLoader(dataset, batch_size=config["batch_size"], shuffle=False)

    # Create and Load Model
    model = create_model(classes=config["classes"], meta_file=meta_file)
    model.load_state_dict(torch.load(model_path))
    model = model.to(device)
    model.eval()

    correct = 0
    total = 0

    # Evaluation Loop
    with torch.no_grad():
        for images, labels in data_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    accuracy = 100 * correct / total
    print(f"Accuracy: {accuracy:.2f}%")
    return {"accuracy": accuracy}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate a XXX model.")
    parser.add_argument("-i", "--input_dir", type=str, required=True, help="Path to validation data.")
    parser.add_argument("-m", "--meta_file", type=str, required=True, help="Path to metadata file.")
    parser.add_argument("-p", "--model_path", type=str, required=True, help="Path to the trained model.")
    parser.add_argument("-b", "--batch_size", type=int, default=16, help="Batch size for evaluation.")
    parser.add_argument("-g", "--device", type=str, default="cuda:0", help="Device for evaluation.")
    parser.add_argument("-c", "--classes", nargs="+", required=True, help="List of ship classes.")
    args = parser.parse_args()

    evaluate_model(
        data_dir=args.data_dir,
        meta_file=args.meta_file,
        model_path=args.model_path,
        device=args.device,
        config=vars(args),
    )

