# NIIVTB: Vietnamese Phrase-Structure Treebank
NIIVTB is a Vietnamese constituent treebank that is annotated with three layers: word segmentation, part-of-speech tagging, and bracketing. This treebank includes 20,588 sentences divided into two subsets, NIIVTB-1 (10,431 sentences) and NIIVTB-2 (10,157 sentences), corresponding to two different sets of raw texts: [VLSP](https://vlsp.hpda.vn/) and our original texts. The raw texts of VLSP, downloaded from Youth (Tuổi Trẻ) - an online daily newspaper, are focused on social and political topics. Our original texts, which were collected from a Vietnamese online newspaper - [Thanhnien news](https://thanhnien.vn), cover 14 topics. We selected an equal number of texts for each topic (please refer to [our LRE paper](https://link.springer.com/article/10.1007/s10579-017-9398-3 "Ensuring Annotation Consistency and Accuracy for Vietnamese Treebank") for more details). Each of NIIVTB-1 and NIIVTB-2 is separated into three parts, Dev including 1000 sentences (files in the Dev directory), Test including 1000 sentences (files in the Test directory), and Train including the rest (files in the Train directory).

Due to the copyright issue, we provide only annotations. In order to obtain a treebank with original raw texts, please follow this procedure.

NIIVTB-1:
1.	Place .raw files of the VLSP treebank (https://vlsp.hpda.vn/) in the directory *"NIIVTB-1-RawText"*
2.	Run *"./merge.py treebank/NIIVTB-1"*
3.	NIIVTB-1 with raw texts are output in *"NIIVTB-1-Finished"*

NIIVTB-2:
1.	Acquire texts from Thanhnien newspaper (https://thanhnien.vn)
2.	Preprocess text:

.. a.	Name the file based on information provided in the file "Thanhnien URLs.txt", for example, the newspaper from *"// URL: http://www.thanhnien.com.vn/kinh-te/scic-tiep-tuc-thoai-von-toan-bo-tai-2-doanh-nghiep-lon-448268.html"* is named as  *"Dev_Economic_0.raw"*

.. b.	Segment sentences, for example:

... Original newspaper:

![alt text](https://github.com/mynlp/niivtb/blob/master/treebank/Ex-PreprocessingText/Ex-OriginalNewspaper.jpg)

... Newspaper after sentence segmentation:

![alt text](https://github.com/mynlp/niivtb/blob/master/treebank/Ex-PreprocessingText/Ex-PreprocessedText.jpg)

3.	Place the preproced texts in the directory *"NIIVTB-2-RawText"*
4.	Run *"./merge.py treebank/NIIVTB-2"*.
5.	NIIVTB-2 with raw texts are output in *"NIIVTB-2-Finished"*

*Note:* If your raw texts are not identical to our texts, the invalid files will be listed in *"invalidFiles.txt"*. This means that the treebank was not created for those files. Please refer to the files in the directory *"NIIVTB-1-ID"* or *"NIIVTB-2-ID"* for modifying your texts. Your texts must have the same name and number of sentences (rows) as the ID files. Number in each row in the ID files indicates number of syllables per sentence that the raw texts must follow. 

This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 2.0 Generic]( https://creativecommons.org/licenses/by-nc-sa/2.0/).

### Tags

POS tags

| No.| POS tag |	Meaning of tag |	No. |	POS tag	| Meaning of tag |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 1	| Sv	| Sino-Vietnamese syllable |	18	| Vcp|	Comparative verb |
| 2	| Nc	| Classifier noun |	19 |	Vv	| Other verb |
| 3	| Ncs	| Special classifier noun	| 20 |	An |	Ordinal number |
| 4	| Nu	| Unit noun |	21	| Aa	| Other adjective |
| 5	|Nun	|Special unit noun|	22|	Pd	|Demonstrative pronoun|
| 6	|Nw|	Quantifier indicating the whole	|23|	Pp|	Other pronoun|
| 7	|Num|	Number|	24|	R	|Adjunct|
| 8	|Nq	|Other quantifier|	25 |	Cs |	Preposition or conjunction introducing a clause |
| 9 |	Nr	|Proper noun| 26| Cp|	Other conjunction|
| 10	|Nt|	Noun of time	| 27	|ON|	Onomatopoeia|
| 11 |	Nn|	Other noun|	28	|ID	|Idioms|
| 12	|Ve|	Exiting verb	| 29	|E|	Exclamation word|
| 13 |	Vc|	Copula "là" verb|30	|M	|Modifier word|	
| 14	|D	|Directional verb|	31|	FW|	Foreign word|
| 15	|VA	|Verb-adjective|32|	X	|Unknown word|	
| 16|	VN|	Verb-noun|	33|	PU	|Punctuation|
| 17	|NA|	Noun-adjective| | | | 

Constituency tags

|No.|	Tag	|Explanation|	No.|	Tag	|Explanation |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
|1|	NP	|Noun phrase	|10|	QRP|	Questioning adjunct phrase|
|2	|QP|	Quantitative phrase|	11|	QPP|	Questioning prepositional phrase|
|3	|VP|	Verb phrase	|12	|QADJP|	Questioning adjective phrase|
|4|	ADJP |	Adjective phrase|	13|	MDP |	Modal phrase|
|5 |	PP |	Prepositional phrase |	14 |	S |	Simple/compound declarative sentence |
|6 |	RP |	Adjunct phrase |	15 |	SQ |	Question |
|7 |	CONJP |	Conjunction phrase |	16 |	SPL |	Special sentence |
|8 |	UCP |	Unlike coordinated phrase |	17	 |SBAR |	Subordinate clause |
|9 |	QNP |	Questioning noun phrase |	18 |	XP |	Unknown phrase |

Functional tags 

| No.	| Tag	|	Explanation	|	No.	|	Tag	|	Explanation	|
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 1	|	H	|	Head of phrase	|	12	|	TMP	|	Temporal	|
| 2	|	SBJ	|	Subject	|	13	|	LOC	|	Locative	|
| 3	|	LGS	|	Logical subject	|	14	|	MNR	|	Manner	|
| 4	|	PRD	|	Predicate that is not VP	|	15	|	PRP	|	Purpose or reason	|
| 5	|	DOB	|	Direct object	|	16	|	CND	|	Condition	|
| 6	|	IOB	|	Indirect object	|	17	|	CNC	|	Concessions	|
| 7	|	CMP	|	Complement	|	18	|	ADV	|	Adverbial	|
| 8	|	TPC	|	Topicalized	|	19	|	HLN	|	Headline	|
| 9	|	MDP	|	Modal phrase	| 20	|	TTL	|	Title	|
| 10	|	VOC	|	Vocative	|	21	|	EXC	|	Exclamative sentence	|
| 11	|	PRN	|	Parenthetical	|	22	|	CMD	|	Imperative sentence	| 

Null elements 

| No. |	Tag |	Explanation | 
| ------------- | ------------- | ------------- |
| 1 |	\*T\* |	Trace of phrase movement |
| 2 |	\*E\* |	Ellipses without trace for phrase |
| 3 |	* |	Ellipses with trace for phrase |
| 4 |	\*0\* |	Null complementizer |
| 5 |	\*P\* |	Null passive verb |
| 6 |	\*H\* |	Ellipses with trace for head word |
| 7 |	\*D\* |	Ellipses with trace for direct object of reduced relative clause | 

Word-internal structure tags 

| Group |	Tag |	Description |
| ------------- | ------------- | ------------- |
| Word |	Nn_w |	A combination of one or more Sino-Vietnamese elements and an original Vietnamese word to create a noun  |
| |	Vv_w |	A combination of a Sino-Vietnamese element and an original Vietnamese word to create a verb  |
| | 	Aa_w |	A combination of a Sino-Vietnamese element and an original Vietnamese word to create an adjective  |
| | 	R_w |	A combination of a Sino-Vietnamese element and an original Vietnamese word to create an adjunct  |
| Supra-word sub-phrase |	Nn_swsp |	A sequence of a classifier noun (Nc) and its modifier that has meaning as a noun |
| 	| Nn_swsp |	A sequence of a special classifier noun (Ncs) and its modifier that has meaning as a noun |
| | 	Nn_swsp |	A sequence of a categorization noun (Nn) and its modifier that has meaning as a noun |
| | 	Vv_swsp_Rt |	A repetitive form that has meaning as a verb |
| | 	Aa_swsp_Rt |	A repetitive form that has meaning as an adjective |
| | 	Nn_swsp_Rt |	A repetitive form that has meaning as a noun |
| |	On_swsp_Rt |	A repetitive form is a sound |

Details of these tags are available in our LRE paper.

### Publications:

1.	Quy T. Nguyen, Yusuke Miyao, Ha T.T. Le, Nhung T.H. Nguyen. 2018. *[Ensuring Annotation Consistency and Accuracy for Vietnamese Treebank](https://link.springer.com/article/10.1007/s10579-017-9398-3)*. Language Resources and Evaluation, 52(1), pages: 269-315.
2.	Quy T. Nguyen, Yusuke Miyao, Ha T.T. Le, Ngan L.T. Nguyen. 2016.  *[Challenges and Solutions for Consistent Annotation of Vietnamese Treebank](http://www.lrec-conf.org/proceedings/lrec2016/pdf/95_Paper.pdf)*. In proceedings of 10th edition of the Language Resources and Evaluation Conference, pages: 1532-1539.
