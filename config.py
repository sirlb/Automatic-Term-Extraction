# -*- coding: utf-8 -*-


base_path = 'pretraining_models/'

def model_backbone_path(model_backbone):
    
    if model_backbone == 'roberta_wwm_ext':
        config_path = base_path + 'chinese_roberta_wwm_ext_L-12_H-768_A-12/bert_config.json'
        checkpoint_path = base_path + 'chinese_roberta_wwm_ext_L-12_H-768_A-12/bert_model.ckpt'
        dict_path = base_path + 'chinese_roberta_wwm_ext_L-12_H-768_A-12/vocab.txt'
    
    elif model_backbone == 'roberta_wwm_ext_kg':
        config_path = base_path + 'chinese_roberta_wwm_ext_L-12_H-768_A-12-kg/bert_config.json'
        checkpoint_path = base_path + 'chinese_roberta_wwm_ext_L-12_H-768_A-12-kg/bert_model.ckpt'
        dict_path = base_path + 'chinese_roberta_wwm_ext_L-12_H-768_A-12-kg/vocab.txt'
        
    elif model_backbone == 'bert':
        config_path = base_path + 'chinese_L-12_H-768_A-12/bert_config.json'
        checkpoint_path = base_path + 'chinese_L-12_H-768_A-12/bert_model.ckpt'
        dict_path = base_path + 'chinese_L-12_H-768_A-12/vocab.txt'
    
    elif model_backbone == 'bert_wwm_ext':
        config_path = base_path + 'chinese_wwm_ext_L-12_H-768_A-12/bert_config.json'
        checkpoint_path = base_path + 'chinese_wwm_ext_L-12_H-768_A-12/bert_model.ckpt'
        dict_path = base_path + 'chinese_wwm_ext_L-12_H-768_A-12/vocab.txt'
        
    elif model_backbone == 'bert_wwm':
        config_path = base_path + 'chinese_wwm_L-12_H-768_A-12/bert_config.json'
        checkpoint_path = base_path + 'chinese_wwm_L-12_H-768_A-12/bert_model.ckpt'
        dict_path = base_path + 'chinese_wwm_L-12_H-768_A-12/vocab.txt'    
    
    elif model_backbone == 'roberta_wwm_large_ext':
        config_path = base_path + 'chinese_roberta_wwm_large_ext_L-24_H-1024_A-16/bert_config.json'
        checkpoint_path = base_path + 'chinese_roberta_wwm_large_ext_L-24_H-1024_A-16/bert_model.ckpt'
        dict_path = base_path + 'chinese_roberta_wwm_large_ext_L-24_H-1024_A-16/vocab.txt'
    
    
    return config_path,checkpoint_path,dict_path


def dataset_path(dataset):

        
    if dataset == 'math_ate':
        train_path = 'data/ate_dataset/math/all/train.bio'
        dev_path = 'data/ate_dataset/math/all/dev.bio'
        test_path = 'data/ate_dataset/math/all/test.bio'
    
    elif dataset == 'math_ate_10':
        train_path = 'data/ate_dataset/math/10/train.bio'
        dev_path = 'data/ate_dataset/math/10/dev.bio'
        test_path = 'data/ate_dataset/math/10/test.bio'
        
    elif dataset == 'math_ate_50':
        train_path = 'data/ate_dataset/math/50/train.bio'
        dev_path = 'data/ate_dataset/math/50/dev.bio'
        test_path = 'data/ate_dataset/math/50/test.bio'
        
    elif dataset == 'math_ate_100':
        train_path = 'data/ate_dataset/math/100/train.bio'
        dev_path = 'data/ate_dataset/math/100/dev.bio'
        test_path = 'data/ate_dataset/math/100/test.bio'
    elif dataset == 'math_ate_500':
        train_path = 'data/ate_dataset/math/500/train.bio'
        dev_path = 'data/ate_dataset/math/500/dev.bio'
        test_path = 'data/ate_dataset/math/500/test.bio'
        
    return train_path,dev_path,test_path