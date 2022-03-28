#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 10:01:27 2019

@author: Shuowen Wei, k26609
"""

import torch
import torch.nn as nn
import torch.nn.functional as F

class PureCNN(nn.Module):
    
    def __init__(self, lstDrops, nDims, vocabSize, lstKernels, numFilters):
        super(PureCNN, self).__init__()
        self.emb1 = nn.Embedding(vocabSize, nDims)
        self.drop1 = nn.Dropout(p=lstDrops[0])
        self.drop2 = nn.Dropout(p=lstDrops[1])
        Ks = lstKernels
        D = nDims #lstmNodes#*2 #nDims
        Ci = 1
        Co = numFilters
        self.convs1 = nn.ModuleList([nn.Conv2d(Ci, Co, (K, D)) for K in Ks])
        self.drop3 = nn.Dropout(p=lstDrops[2])
        self.linear = nn.Linear(Co*len(Ks), Co*len(Ks))
        self.drop4 = nn.Dropout(p=lstDrops[3])
        self.linOut = nn.Linear(Co*len(Ks), 1)
    def forward(self, x):
        # [batch size, text len] # batch is first 
        x = self.emb1(x)   # x = self.drop1(self.emb1(x)) 
        # [batch size, text len, emb dim] 
        x = x.unsqueeze(1)  # (N, Ci, W, D)
        # [batch size, 1, text len, emb dim] 
        x = [F.relu(conv(x)).squeeze(3) for conv in self.convs1]  # [(N, Co, W), ...]*len(Ks)
        x = [F.max_pool1d(i, i.size(2)).squeeze(2) for i in x]  # [(N, Co), ...]*len(Ks)
        # [ batch size, Co ] * len(Ks)
        x = torch.cat(x, dim=1)
        # [batch size, 1, emb dim * len(Ks) ] 
        x = self.drop3(x)
        x = F.relu(self.linear(x))
        x = self.drop4(x)
        x = self.linOut(x)
        return x

    
class LSTMNet(nn.Module):
    def __init__(self, lstDrops, lstmNodes, nDims, vocabSize, nLayers):
        super(LSTMNet, self).__init__()
        self.emb1 = nn.Embedding(vocabSize, nDims)
        self.drop1 = nn.Dropout(p=lstDrops[0])
        self.lstm = nn.LSTM(nDims, lstmNodes, dropout=lstDrops[1], batch_first=True, num_layers=nLayers)#), bidirectional=True) # batch_first=True 
        self.drop2 = nn.Dropout(p=lstDrops[2])
        self.linOut = nn.Linear(lstmNodes, 1)
    def forward(self, x):
        x = self.emb1(x)
        out1, _ = self.lstm(x)
        x = self.drop2(out1[:, -1, :]) # if batch_first = False (default), it should be out1[-1, :, :]
        x = self.linOut(x)
        return x
    
    
class LSTMNet_V2(nn.Module):
    def __init__(self, lstDrops, lstmNodes, nDims, vocabSize, nLayers):
        super(LSTMNet_V2, self).__init__()
        self.emb1 = nn.Embedding(vocabSize, nDims)
        self.drop1 = nn.Dropout(p=lstDrops[0])
        self.lstm = nn.LSTM(nDims, lstmNodes, dropout=lstDrops[1], num_layers=nLayers, bidirectional=True) # batch_first=True
        self.drop2 = nn.Dropout(p=lstDrops[2])
        self.linOut = nn.Linear(lstmNodes*2, 1)
    def forward(self, x):
        x = x.permute(1,0)
        x = self.emb1(x)
        output, (hidden, cell) = self.lstm(x) 
        hidden = self.drop2(torch.cat((hidden[-2,:,:], hidden[-1,:,:]), dim=1))
        x = self.linOut(hidden.squeeze(0)) 
        return x


class LSTM_CNN(nn.Module):
#     def conv_and_pool(self, x, conv):
#         print(" *** *** conv_and_pool input x size: ", x.size())        #---> torch.Size([96, 1, 3000, 256])
#         x = F.relu(conv(x)).squeeze(3)  # (N, Co, W)
#         print(" *** *** conv_and_pool relu x size: ", x.size())
#                             #---> torch.Size([96, 50, 2998])
#                             #---> torch.Size([96, 50, 2997])
#                             #---> torch.Size([96, 50, 2996])
#         x = F.max_pool1d(x, x.size(2)).squeeze(2)
#         print(" *** *** conv_and_pool max_pool1d x size: ", x.size())
#                             #---> torch.Size([96, 50])
#                             #---> torch.Size([96, 50])
#                             #---> torch.Size([96, 50])
#         return x

    def __init__(self, lstDrops, lstmNodes, nDims, vocabSize, nLayers, lstKernels, numFilters):
        super(LSTM_CNN, self).__init__()
        self.emb1 = nn.Embedding(vocabSize, nDims)
        self.drop1 = nn.Dropout(p=lstDrops[0])
        self.lstm = nn.LSTM(nDims, lstmNodes, dropout=lstDrops[1], num_layers=nLayers, batch_first=True)#, bidirectional=True)
        self.drop2 = nn.Dropout(p=lstDrops[1])
        Ks = lstKernels#[3,4,5,6]
        D = lstmNodes#*2 #nDims
        Ci = 1
        Co = numFilters#100
        self.convs1 = nn.ModuleList([nn.Conv2d(Ci, Co, (K, D)) for K in Ks])
#         self.conv13 = nn.Conv2d(Ci, Co, (3, D))
#         self.conv14 = nn.Conv2d(Ci, Co, (4, D))
#         self.conv15 = nn.Conv2d(Ci, Co, (5, D))
        self.drop3 = nn.Dropout(p=lstDrops[2])
        self.linear = nn.Linear(Co*len(Ks), Co*len(Ks))
        self.drop4 = nn.Dropout(p=lstDrops[3])
        self.linOut = nn.Linear(Co*len(Ks), 1) 
    def forward(self, x):
#         print(" *** input x size: ", x.size())             #---> torch.Size([96, 3000]) # batch first 
#         x = x.permute(1,0)
#         print(" *** after permute x size: ", x.size())
        x = self.emb1(x)  # x = self.drop1(self.emb1(x))
#         print(" *** embedding output size: ", x.size())    #---> torch.Size([96, 3000, 100])
        
        output, (hidden, cell) = self.lstm(x)
#         print(" *** lstm output - output size: ", output.size())  #---> torch.Size([96, 3000, 256])
#         print(" *** lstm output - hidden size: ", hidden.size())  #---> torch.Size([2, 96, 256])

#         hidden = self.drop2(torch.cat((hidden[-2,:,:], hidden[-1,:,:]), dim=1))
#         print(" *** cat hidden size: ", hidden.size())          #*---> torch.Size([96, 512]) 
        output = self.drop2(output) 
#         x = output.unsqueeze(1) 
#         print(" *** after unsqueeze(1): ", x.size())       #---> torch.Size([96, 1, 3000, 256])
#         x1 = self.conv_and_pool(x, self.conv13) #(N,Co)
#         print(" *** x1 : ", x1.size())                     #---> torch.Size([96, 50])
#         x2 = self.conv_and_pool(x, self.conv14) #(N,Co)
#         print(" *** x2 : ", x2.size())                     #---> torch.Size([96, 50])
#         x3 = self.conv_and_pool(x, self.conv15) #(N,Co)
#         print(" *** x3 : ", x3.size())                     #---> torch.Size([96, 50])
#         x = torch.cat((x1, x2, x3), 1) # (N,len(Ks)*Co)
#         print(" *** torch.cat x1,x2,x3 --> x: ", x.size()) #---> torch.Size([96, 150])

        x = output.unsqueeze(1)  # (N, Ci, W, D)
        x = [F.relu(conv(x)).squeeze(3) for conv in self.convs1]  # [(N, Co, W), ...]*len(Ks)
        x = [F.max_pool1d(i, i.size(2)).squeeze(2) for i in x]  # [(N, Co), ...]*len(Ks)
        x = torch.cat(x, dim=1)
        
        x = self.drop3(x)
#         print(" *** after drop out 3: ", x.size())         #---> torch.Size([96, 150])
        x = F.relu(self.linear(x))
        x = self.drop3(x)
        x = self.linOut(x)
#         print(" *** after linear: ", x.size())             #---> torch.Size([96, 1])
        return x


import torch
import torch.nn as nn

from sklearn.metrics import confusion_matrix, roc_curve, auc
from scipy import interp
import matplotlib.pyplot as plt

def confusion(truth, prediction):
    confusion_vector = prediction / truth

    true_positives = torch.sum(confusion_vector == 1).item()
    false_positives = torch.sum(confusion_vector == float('inf')).item()
    true_negatives = torch.sum(torch.isnan(confusion_vector)).item()
    false_negatives = torch.sum(confusion_vector == 0).item()
#     print(confusion_vector)
    return true_positives, false_positives, true_negatives, false_negatives


def adjust_learning_rate(optimizer, init_lr, epoch):
    """Sets the learning rate to the initial LR decayed by 10 every 30 epochs"""
#     if epoch >= 150 and epoch % 30 == 0:
#         lr = init_lr * (0.5 ** ((epoch-150) // 30))
#         print('Learning Rate lr is reset to {}'.format(lr))
#         for param_group in optimizer.param_groups:
#             param_group['lr'] = lr
#         return optimizer
    if epoch % 30 == 0:
        lr = init_lr * (0.5 ** (epoch // 30))
        print('Learning Rate lr is set to {}'.format(lr))
        for param_group in optimizer.param_groups:
            param_group['lr'] = lr
    return optimizer

def binary_accuracy(preds, y):
    """
    Returns accuracy per batch, i.e. if you get 8/10 right, this returns 0.8, NOT 8
    """
    #round predictions to the closest integer
    rounded_preds = torch.round(torch.sigmoid(preds))
    correct = (rounded_preds == y).float() #convert into float for division 
    acc = correct.sum()/len(correct)
    return acc

def train(model, iterator, optimizer, criterion, device):
    epoch_loss = 0
    epoch_acc = 0
    model.train()
    for x, y in iterator: #tqdm.tqdm(iterator):
        x, y = x.to(device), y.to(device).unsqueeze(1)
        optimizer.zero_grad()
        preds = model(x)
        loss = criterion(preds, y)
        acc = binary_accuracy(preds, y)

        loss.backward()
        optimizer.step()
#         optimizer = adjust_learning_rate(optimizer, init_lr, epoch) # adjust learning rate here 

        epoch_loss += loss.item() # need * x[0] when in multi-label mode 
        epoch_acc += acc.item()
        
    return epoch_loss / len(iterator), epoch_acc / len(iterator)

def evaluate(model, iterator, criterion, device):
    epoch_loss = 0
    epoch_acc = 0
    model.eval()
    with torch.no_grad():
        for x, y in iterator:#tqdm.tqdm(iterator):
            x, y = x.to(device), y.to(device).unsqueeze(1)
            preds = model(x)
            loss = criterion(preds, y)
            acc = binary_accuracy(preds, y)
            
            epoch_loss += loss.item() # need * x[0] when in multi-label mode 
            epoch_acc += acc.item()
            
    return epoch_loss / len(iterator), epoch_acc / len(iterator)


# for BCEWithLogitsLoss and multi-label in the future  
# compute y_true, y_pred_sigmoid for generating confusion matrix and AUC ROC 
def evaluate_w_confusion(model, iterator, criterion, device, epoch):
    epoch_loss = 0
    epoch_acc = 0
    model.eval()
    all_y_true = None
    all_y_pred = None
    tp, fp, tn, fn = 0, 0, 0, 0 # true_positives, false_positives, true_negatives, false_negatives
    with torch.no_grad():
        for x, y in iterator: #tqdm.tqdm(iterator):
            x, y = x.to(device), y.to(device).unsqueeze(1)
            preds = model(x)
            if all_y_true is None and all_y_pred is None:
                all_y_true = y
                all_y_pred = preds
            else:
                all_y_true = torch.cat((all_y_true, y), 0) 
                all_y_pred = torch.cat((all_y_pred, preds), 0) 
            loss = criterion(preds, y)
#             acc, rounded_preds, confusion, fpr_batch, tpr_batch = binary_accuracy(preds, y) 
            acc = binary_accuracy(preds, y)
            epoch_loss += loss.item() # need * x[0] when in multi-label mode 
            epoch_acc += acc.item()
            
#         tp, fp, tn, fn = confusion(all_y_true, torch.round(torch.sigmoid(all_y_pred)))
        y_true, y_pred_sigmoid = all_y_true.cpu().numpy().flatten(), torch.sigmoid(all_y_pred).cpu().numpy().flatten()
        
    return epoch_loss / len(iterator), epoch_acc / len(iterator), y_true, y_pred_sigmoid #(tp+tn)/(tp+fp+tn+fn)



min_freq = 2
itos = [o for o,c in freq.most_common(max_vocab) if c > min_freq]
# orders matter here, insert _pad_ first 
itos.insert(0, '_pad_')
itos.insert(0, '_unk_') 
stoi = collections.defaultdict(lambda:0, {v:k for k,v in enumerate(itos)})
len(itos)



for cNum, config in enumerate(configs, 1):
    print(f'| cNum: {cNum:03}/{len(configs):03} | Config: {config}')
    resultsDict[str(config)] = [0, 0, 0, 0] # train_loss, train_acc, valid_loss, valid_acc
    # PureCNN
    model = webadv_model.PureCNN(lstDrops=config["drops"], nDims=config["nDims"], vocabSize=CNN_config["vocabSize"],
                                 lstKernels=config["lstKernels"], numFilters = config["numFilters"])
    model.to(device)
    opt = optim.Adam(model.parameters(), lr=0.001, weight_decay=0.0001) # it was 0.001 
    loss_func = nn.BCEWithLogitsLoss()
    loss_func.to(device)
    for epoch in range(1, epochs + 1):
        train_loss, train_acc = webadv_train.train(model, trainLoader, opt, loss_func, device)
        valid_loss, valid_acc = webadv_train.evaluate(model, testLoader, loss_func, device)
        print(f'\t| Epoch: {epoch:02} | Train Loss: {train_loss:.3f} | Train Acc: {train_acc*100:.2f}% | Val. Loss: {valid_loss:.3f} | Val. Acc: {valid_acc*100:.2f}% |')

        if valid_acc > resultsDict[str(config)][3]:
            resultsDict[str(config)] = [train_loss, train_acc, valid_loss, valid_acc]
    # save resultsDict at each round 
    pickle.dump(resultsDict, open(basePath/'tmp'/'resultsDict.pkl', 'wb')) 
    