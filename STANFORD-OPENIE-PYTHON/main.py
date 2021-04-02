from openie import StanfordOpenIE

with StanfordOpenIE() as client:
    text = 'AhnLab ASEC Analysis Team has been monitoring BlueCrab(=Sodinokibi) ransomware in form of Javascript distributed via phishing download page.'
    print('Text: %s.' % text)
    for triple in client.annotate(text):
        print('|-', triple)

    graph_image = 'graph2.png'
    client.generate_graphviz_graph(text, graph_image)
    print('Graph generated: %s.' % graph_image)

    with open('corpus/pg6130.txt', encoding='utf8') as r:
        corpus = r.read().replace('\n', ' ').replace('\r', '')

    triples_corpus = client.annotate(corpus[0:5000])
    print('Corpus: %s [...].' % corpus[0:80])
    print('Found %s triples in the corpus.' % len(triples_corpus))
    for triple in triples_corpus[:3]:
        print('|-', triple)
    print('[...]')
