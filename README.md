# LoRa Propagation Model

This repository houses innovative models designed to enhance LoRa propagation predictions by automating path loss estimation. The project comprises of data collection, training, testing and automation of the model.

## Dataset Creation

- Install the LoRa sender code on one of the designated end-device LoRa node.
- Install the LoRa receiver code on the other designated end-device LoRa node.
- Run the *dataset_creator_sf* python module on the system connected with node hosting receiver.

## Path loss Estimation

- For the GPS coordinates between those the path loss is to be estimated obtain the obstruction data first using *Height_estimation* module.
- Execute the *additional_loss* module to compute the loss caused due to multiwall-floor model.
- Execute the *test_models* module the parameters required and pass bias as the loss computed due to multiwall-floor.
- Compare the proposed model with other models.

## Obstruction Height Estimation

- Install samgeo, leafmap and jupyter modules.
- Run a jupyter server by executing *jupyter notebook* command in the terminal.
- Execute the *Height_estimation.ipynb* notebook in *Height_estimation* module with the required GPS coordinates.
- Execute the *shadow-overlapping_tool.py* module to obtain the obstruction height details.
- Place all the files with height data renamed in order staring from 1 in *obstruction_data* directory.

