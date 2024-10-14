# HAGCN
This repository contains the implementation of the paper "Skeletal Human Action Recognition using Hybrid Attention-based Graph Convolutional Network". The author will maintain it from time to time, but timely feedback is not guaranteed.

## Prerequisites
create the conda environment using the 'environment.yml' file.

## Datasets
Authors used the data generation function from the CTR-GCN repo. 
```
path_to_dataset
    ├── train_data.npz
    ├── test_data.npz
```
## Training
After activating the conda environment, train a model using:
```
python train.py --config ./config/train_hagcn_x.yaml
```
x could 'bone', 'joint', 'bone_motion', 'joint_motion'

## Citation
If you use this code or find our paper helpful, please cite:
```
@inproceedings{xing2022skeletal,
  title={Skeletal human action recognition using hybrid attention based graph convolutional network},
  author={Xing, Hao and Burschka, Darius},
  booktitle={2022 26th International Conference on Pattern Recognition (ICPR)},
  pages={3333--3340},
  year={2022},
  organization={IEEE}
}

@inproceedings{chen2021channel,
  title={Channel-wise topology refinement graph convolution for skeleton-based action recognition},
  author={Chen, Yuxin and Zhang, Ziqi and Yuan, Chunfeng and Li, Bing and Deng, Ying and Hu, Weiming},
  booktitle={Proceedings of the IEEE/CVF international conference on computer vision},
  pages={13359--13368},
  year={2021}
}
```
