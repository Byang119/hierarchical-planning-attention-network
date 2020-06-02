import argparse

class Hparams:
    parser = argparse.ArgumentParser()

    # prepro
    parser.add_argument('--vocab_size', default=30000, type=int)
    parser.add_argument('--lvocab_size', default=6000, type=int)
    parser.add_argument('--pvocab_size', default=35, type=int)


    # train
    ## files
    parser.add_argument('--train1', default='prepro/ordered/train.o_label',
                        help="keys training segmented data")
    parser.add_argument('--train2', default='prepro/ordered/train.infobox',
                        help="infobox (including all the keys, positions and values) training segmented data")
    parser.add_argument('--train3', default='prepro/ordered/train.summary',
                        help="reference summary training segmented data")

    parser.add_argument('--eval1', default='prepro/ordered/eval.o_label',
                             help="keys evaluation segmented data")
    parser.add_argument('--eval2', default='prepro/ordered/eval.infobox',
                        help="infobox (including all the keys, positions and values) evaluation segmented data")
    parser.add_argument('--eval3', default='prepro/eval.summary',
                        help="reference summary evaluation segmented data")

    ## vocabulary
    parser.add_argument('--vocab', default='prepro/vocab',
                        help="vocabulary file path")
    parser.add_argument('--lvocab', default='prepro/label.vocab',
                        help="label vocabulary file path")
    parser.add_argument('--pvocab', default='prepro/pos.vocab',
                        help="position vocabulary file path")

    # training scheme
    parser.add_argument('--batch_size', default=128, type=int)
    parser.add_argument('--eval_batch_size', default=128, type=int)

    parser.add_argument('--lr', default=0.003, type=float, help="learning rate")
    parser.add_argument('--warmup_steps', default=4000, type=int)
    parser.add_argument('--logdir', default="log/1", help="log directory")
    parser.add_argument('--num_epochs_plan', default=10, type=int)
    parser.add_argument('--num_epochs', default=30, type=int)
    parser.add_argument('--evaldir', default="eval/1", help="evaluation dir")

    # model
    parser.add_argument('--d_model', default=300, type=int,
                        help="embedding dimension and hidden dimension of attribute_encoder/decoder")
    parser.add_argument('--d_ff', default=600, type=int,
                        help="hidden dimension of feedforward layer")
    parser.add_argument('--num_blocks', default=2, type=int,
                        help="number of encoder/decoder blocks")
    parser.add_argument('--num_heads', default=6, type=int,
                        help="number of attention heads")
    parser.add_argument('--topk', default=6, type=int,
                        help="selection scale of word_level planning")
    parser.add_argument('--topk2', default=15, type=int,
                        help="selection scale of attribute-level planning")
    parser.add_argument('--maxlen1', default=19, type=int,
                        help="maximum of input attributes")
    parser.add_argument('--maxlen2', default=20, type=int,
                        help="maximum length of each attributes")
    parser.add_argument('--maxlen3', default=60, type=int,
                        help="maximum length of a target sequence")
    parser.add_argument('--dropout_rate', default=0.3, type=float)
    parser.add_argument('--smoothing', default=0.1, type=float,
                        help="label smoothing rate")

    # test

    parser.add_argument('--eval1', default='prepro/ordered/test.o_label',
                        help="keys test segmented data")
    parser.add_argument('--eval2', default='prepro/ordered/test.infobox',
                        help="infobox (including all the keys, positions and values) test segmented data")
    parser.add_argument('--eval3', default='prepro/test.summary',
                        help="reference summary test segmented data")


    parser.add_argument('--ckpt', help="checkpoint file path")
    parser.add_argument('--test_batch_size', default=128, type=int)
    parser.add_argument('--testdir', default="test", help="test result dir")