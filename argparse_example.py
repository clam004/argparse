if __name__ == "__main__":
    '''
    (venv310) carsonlam@MacBook-Pro notebooks % python args.py 10 2                        
    2 10 32
    '''
    import argparse
    parser = argparse.ArgumentParser(description='simple distributed training job')
    parser.add_argument('total_epochs', type=int, help='Total epochs to train the model')
    parser.add_argument('save_every', type=int, help='How often to save a snapshot')
    parser.add_argument('--batch_size', default=32, type=int, help='Input batch size on each device (default: 32)')
    args = parser.parse_args()

    print(args.save_every, args.total_epochs, args.batch_size)