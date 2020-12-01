import org.junit.jupiter.api.RepeatedTest;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.Random;
import java.util.Stack;

class TestAVLTree {

  private final static String ALLOWED_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890";
  private final static int ITEM_NUM = 1000;

  private Random mRandom = new Random();
  
  @RepeatedTest(100)
  void testFind() {

    AVLTree avlTree = new AVLTree();
    String findMe = generateRandomString(6);

    avlTree.insert(findMe);
    for (int i = 0; i < ITEM_NUM; i++) {
      avlTree.insert(generateRandomString(6));
    }

    assertTrue(avlTree.inTree(findMe));
  }

  @RepeatedTest(100)
  void testBalenced() {

    AVLTree avlTree = new AVLTree();
    for (int i = 0; i < ITEM_NUM; i++) {
      avlTree.insert(generateRandomString(6));
    }

    assertTrue(avlTree.isBalenced());
  }

  String generateRandomString(int length) {
    StringBuilder builder = new StringBuilder();
    for (int i = 0; i < length; i++) {
      int index = mRandom.nextInt(ALLOWED_CHARS.length());
      builder.append(ALLOWED_CHARS.subSequence(index, index + 1));
    }
    return builder.toString();
  }
}
