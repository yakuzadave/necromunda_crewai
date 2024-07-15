```
# Import necessary libraries
import pandas as pd
import torch
from transformers import BertForSequenceClassification, BertTokenizer
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load the dataset
df = pd.read_csv('dataset.csv')

# Preprocess the data
X = df['text']
y = df['label']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the BERT tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Preprocess the text data
train_encodings = tokenizer.batch_encode_plus(X_train, 
                                              add_special_tokens=True, 
                                              max_length=512, 
                                              return_attention_mask=True, 
                                              return_tensors='pt')
test_encodings = tokenizer.batch_encode_plus(X_test, 
                                             add_special_tokens=True, 
                                             max_length=512, 
                                             return_attention_mask=True, 
                                             return_tensors='pt')

# Initialize the BERT model for classification
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', 
                                                      num_labels=len(set(y_train)))

# Define the training loop
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

optimizer = torch.optim.Adam(model.parameters(), lr=1e-5)
loss_fn = torch.nn.CrossEntropyLoss()

for epoch in range(5):
    model.train()
    total_loss = 0
    for batch in train_encodings:
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        labels = batch['labels'].to(device)
        optimizer.zero_grad()
        outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
        loss = loss_fn(outputs, labels)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    print(f'Epoch {epoch+1}, Loss: {total_loss / len(train_encodings)}')

    model.eval()
    total_correct = 0
    with torch.no_grad():
        for batch in test_encodings:
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            labels = batch['labels'].to(device)
            outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
            _, predicted = torch.max(outputs.scores, 1)
            total_correct += (predicted == labels).sum().item()
    accuracy = accuracy_score(y_test, predicted.cpu().numpy())
    f1 = f1_score(y_test, predicted.cpu().numpy(), average='macro')
    print(f'Epoch {epoch+1}, Accuracy: {accuracy:.4f}, F1-score: {f1:.4f}')
```

This code provides a basic template for fine-tuning a BERT-based classification model on the labeled dataset. It includes snippets for package import, data handling, model definition, and training. The code assumes that the dataset is stored in a CSV file named 'dataset.csv' and that the text data is stored in a column named 'text', and the label data is stored in a column named 'label'. The code also assumes that the BERT model is pre-trained on the 'bert-base-uncased' dataset.