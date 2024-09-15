# The-Globalizing-K-Pop-Project--Sentiment-Analysis-of-K-Pop-fandoms-on-Social-Media Using Topic Modelling and Large Language Models


## ABSTRACT: 
Social media platforms like Twitter and Reddit have become pivotal spaces for online discussions, significantly reshaping connections and bonds among individuals. This study focuses on K-pop fandoms, characterized by their high engagement and the personal connections fostered by idols through social media. The research explores emotions, opinions, and support networks within these communities, emphasizing the cultural impact of K-pop and its role in fostering global interconnectedness.
Topic modelling and natural language processing techniques were employed to analyse discussions on Twitter and Reddit. The models applied include Latent Dirichlet Allocation (LDA), Non-Negative Matrix Factorization (NMF), BERTopic, and Latent Semantic Analysis (LSA), with Large Language Models (LLMs) aiding in topic interpretation. NMF outperformed other models with a coherence score of 0.656, while LDA and BERTopic scored 0.59, and LSA scored 0.41. Coherence scores between 0.4 and 0.7 indicate good model performance, showing that the topic clusters formed have clear semantic meaning.
The analysis revealed that emotional support is the most prevalent form of social support within K-pop fandoms on Twitter. The findings highlight the distinct roles of Twitter and Reddit in these communities, with Twitter emerging as a stronger platform for emotional and social support. At the same time, Reddit primarily focused on idol appraisal with less emphasis on emotional connections. This study offers valuable insights into the social dynamics of K-pop fandoms, demonstrating how each platform uniquely contributes to the support structures within these online communities.

## INTRODUCTION
Topic modelling, a method traditionally used to uncover underlying themes in a corpus of text, is increasingly leveraged in sentiment analysis to provide a more general understanding of sentiments across different topics within large datasets.[1] This project specifically focuses on K-pop fandoms, known for their high levels of engagement and the personal connections fostered by idols through social media. The core objective of this research is to explore the presence and nature of social support within these communities, guided by Gottlieb's Social Psychological social support model, which identifies various forms of support, including emotional, informational, and appraisal.
To achieve this, the study employs topic modelling techniques—such as Latent Dirichlet Allocation (LDA), Non-Negative Matrix Factorization (NMF), and BERTopic—to analyze discussions on Twitter and Reddit. These techniques are chosen over sentiment analysis to focus on uncovering underlying themes rather than just emotional tone. The motivation behind this research lies in filling a gap in the existing literature, where the dynamics of social support within fandoms, especially through topic modelling, have been underexplored.
Previous studies have touched on the influence of social media on community building and fan engagement, but few have delved into the specific ways social support is structured and expressed within fandoms (Smith, 2020; Lee & Park, 2019). By applying topic modelling to K-pop fandoms' social media activity, this research provides new insights into how these platforms facilitate different forms of social support, contributing to the broader understanding of online community dynamics.


![image](https://github.com/user-attachments/assets/131cb07a-3b56-4fba-81e9-4cdf280fa618)

 
                                 Fig 5: Research Methodology


## 	RESULTS

##### 	Coherence Score of Topic Models 
                             Table 1. Comparison of Coherence Scores of different models
 
![image](https://github.com/user-attachments/assets/81c05bb6-c4e8-4e0c-a083-540ce1581258)


![image](https://github.com/user-attachments/assets/c6da9478-688d-4b41-ae89-67c76f4363cd)


![image](https://github.com/user-attachments/assets/efe6025f-0aff-44d1-82cf-e5cff29555c1)


### Deployed link for the visualization is given below:

https://aditisatsangi.github.io/Globalizing-K-Pop-Project-Analysing-Social-Support-using-Topic-Modelling-and-LLMs/#topic=0&lambda=1&term=


![image](https://github.com/user-attachments/assets/29849a81-df5e-49de-a69b-d6882fb541d5)

 
                          Fig. 9 pyLDAVis Visualization for NMF model 
 

![image](https://github.com/user-attachments/assets/436fe714-8756-49c7-92a7-0270d1216977)


![image](https://github.com/user-attachments/assets/eac3f8e9-5f69-4712-b712-f3713fee06c4)

Fig 12. Results from the representation models

 
## CONCLUSION

#### Best Model and Key Findings
Non-Negative Matrix Factorization (NMF) emerged as the optimal topic model for our analysis, achieving a coherence score of 0.656. Our investigation of Twitter conversations using NMF and PyLDAvis revealed a strong presence of social support within K-Pop online communities. Emotional support constituted the most prevalent form, accounting for 46.6% of tokens.
While LDA and BERTopic exhibited average performance with coherence scores of 0.599 and 0.59 respectively, and LSA demonstrated a lower coherence score of 0.41, these models still contributed to the overall understanding of the topic space. Notably, the performance of BERTopic using Voyage AI embeddings was comparable to that of TF-IDF embeddings, indicating the potential for further exploration of different embedding techniques.

#### 	Consistency in Findings
All four topic models consistently identified core themes related to social support. Emotional support was primarily linked to discussions of personal challenges, while appraisal support was evident in opinion-sharing and achievement-focused conversations. Informational support surfaced in academic-related discussions and merchandise purchases, and instrumental support was observed in conversations about purchasing processes and events.

#### 	Model Combination and Limitations
The combined application of topic modelling and large language models enabled the comprehensive identification of social support within the analysed text. However, challenges were encountered in effectively detecting social-emotional support within Reddit data compared to Twitter data.

Overall, this study demonstrates the efficacy of combining topic modelling and LLMs to uncover the multifaceted nature of social support within K-pop fandoms on social media.




## Additional Files:
#### Poster:  
Research poster presented at the CEPS Undergraduate Poster Session, University of Guelph, Canada.
![image](https://github.com/user-attachments/assets/d38a69a5-965b-4c80-bcfe-b97833bde03f)






