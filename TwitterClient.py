class TwitterClient:
    
        #!/usr/bin/env python

"""
Twitter Client Class



This is the file to connect to Twitter CLient
"""

def main():
    dataset = load_loan_defaulters()
    design_matrix = [row[:-1] for row in dataset]
    target_values = [row[-1] for row in dataset]
    clf = NaiveBayes(extract_features)
    clf.fit(design_matrix, target_values)
    prediction = clf.predict_record([1, 1, 50700])
    negation_word = " not " if prediction == 0.0 else ""
    print("We predict this person will" + negation_word + "default on their loans.")


def extract_features(feature_vector):
    """Maps a feature vector to whether each feature is continuous or discrete."""
    return [
        DiscreteFeature(feature_vector[0]),
        DiscreteFeature(feature_vector[1]),
        ContinuousFeature(feature_vector[2])
    ]


if __name__ == '__main__':
    main()

        
   
        
    
        
        
        
