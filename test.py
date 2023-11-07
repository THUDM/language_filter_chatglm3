forced_lang="Chinese"
glm_path="/data1/zouxu/chatglm3-6b"
from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained(glm_path, trust_remote_code=True)
model = AutoModel.from_pretrained(glm_path, trust_remote_code=True).half().cuda()
model = model.eval()
import random
random.seed(2228)
if forced_lang=="English":
    forced_tokens=open("english-150000")
else:
    forced_tokens=open("chinese-150000")
token_lines=forced_tokens.readlines()
avi_tokens=set()

for l in token_lines:
    lsp=l.split()
    #print(lsp,len(avi_tokens))
    avi_tokens.add(''.join(lsp[:-1]))

    avi_tokens.update(lsp[:-1])
#print(len(avi_tokens))
vcb_size=tokenizer.vocab_size-10
removed_token_list=[]

for i in range(vcb_size):
    opt=tokenizer.decode([i])
    if forced_lang=="English":
        wt=False
        for it in opt:
            wx=False
            if (ord(it)>=48 and ord(it)<=57) or (ord(it)>=65 and ord(it)<=90) or (ord(it)>=97 and ord(it)<=122) or it in ['<','>','|','\n',' ',',','.','\t']:
                wx=True
            else:
                wt=True
        if not(wt):
            avi_tokens.add(opt)
    if forced_lang=="Chinese":
        for it in opt:
            if it in ['<','>','|','\n','\t']:
                avi_tokens.add(opt)

    if not(opt in avi_tokens):
        removed_token_list.append(i)
        #if i%1000==0:
        #print(i,opt)
#print(len(removed_token_list),removed_token_list[0:100])

response, history = model.chat(tokenizer, "Indonesia Geography", history=[],banned_tokens=removed_token_list)
print(response)
