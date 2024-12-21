# -*- coding: utf-8 -*-
'''
@Time          : 2024/12/18 00:00
@Author        : Shinhye Han
@File          : train.py
@Noice         : 
@Description   : Train a XXX model.
@How to use    : python train.py -i {input_dir} -m {meta_file} -o {output_dir} -c {classes} -e {epochs}

@Modificattion :
    @Author    :
    @Time      :
    @Detail    :
'''

import argparse
from torch.utils.data import DataLoader
from torch import optim
from torch.nn import CrossEntropyLoss
from utils.datasets import Dataset
from models.model_selector import create_model
import torch


def train_model(data_dir, meta_file, device, config):
    """
    Train the model on the dataset.

    Args:
        data_dir (str): Path to the training dataset.
        meta_file (str): Path to the metadata file.
        device (torch.device): Device to use for training.
        config (dict): Configuration dictionary with training parameters.

    Returns:
        None
    """
    # Dataset and DataLoader
    dataset = Dataset(input_dir, classes=config["classes"], transforms=None)
    data_loader = DataLoader(dataset, batch_size=config["batch_size"], shuffle=True)

    # Create Model
    model = create_model(classes=config["classes"], meta_file=meta_file)
    model = model.to(device)

    # Define optimizer and loss function
    optimizer = optim.Adam(model.parameters(), lr=config["learning_rate"])
    criterion = CrossEntropyLoss()

    # Training Loop
    for epoch in range(config["epochs"]):
        model.train()
        epoch_loss = 0

        for images, labels in data_loader:
            images, labels = images.to(device), labels.to(device)

            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            epoch_loss += loss.item()

        print(f"Epoch {epoch + 1}/{config['epochs']}, Loss: {epoch_loss:.4f}")

    # Save the model
    torch.save(model.state_dict(), f"{config['output_dir']}/model.pt")
    print(f"Model saved to {config['output_dir']}/model.pt")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train a ship classification model.")
    parser.add_argument("-d", "--input_dir", type=str, required=True, help="Path to training data.")
    parser.add_argument("-m", "--meta_file", type=str, required=True, help="Path to metadata file.")
    parser.add_argument("-o", "--output_dir", type=str, required=True, help="Directory to save the model.")
    parser.add_argument("-b", "--batch_size", type=int, default=16, help="Batch size for training.")
    parser.add_argument("-e", "--epochs", type=int, default=10, help="Number of training epochs.")
    parser.add_argument("-l", "--learning_rate", type=float, default=0.001, help="Learning rate for optimizer.")
    parser.add_argument("-g", "--device", type=str, default="cuda:0", help="Device for training.")
    parser.add_argument("-c", "--classes", nargs="+", required=True, help="List of ship classes.")
    args = parser.parse_args()

    train_model(
        data_dir=args.input_dir,
        meta_file=args.meta_file,
        device=args.device,
        config=vars(args),
    )

