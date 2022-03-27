package com.corenlptest;
import edu.stanford.nlp.simple.*;
import edu.stanford.nlp.trees.Tree;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Main {

    public static void main(String[] args) {
        String content = "";
        try {
            content = Files.readString(Paths.get("hp.txt"));
        } catch (IOException e) {
            e.printStackTrace();
        }
        Document doc = new Document(content);
        Sentence sent = doc.sentence(0);
        System.out.println("Sentence: " + sent);
        for (Tree subtree : sent.parse().subTrees()) {
            System.out.println("Subtree: " + subtree);
        }
    }
}
