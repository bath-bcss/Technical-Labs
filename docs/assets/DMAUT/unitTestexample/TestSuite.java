import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class TestSuite {

  Contact[] test1 = new Contact[] {
    new Contact("C", "C"),
    new Contact("A", "B"),
    new Contact("B", "A"),
    new Contact("B", "B"),
    new Contact("A", "A")
  };

  Contact[] test2 = new Contact[] {
    new Contact("", "9"),
    new Contact("", "8"),
    new Contact("", "7"),
    new Contact("", "6"),
    new Contact("", "5"),
    new Contact("", "4"),
    new Contact("", "3"),
    new Contact("", "2"),
    new Contact("", "1"),
    new Contact("", "0")
  };

  public TestSuite() {
    Arrays.sort(test1);
    Arrays.sort(test2);
  }
 
  @Test
  void testSelection() {
    Contact[] testArray1 = Arrays.copyOf(test1, test1.length);
    List<Contact> testList1 = Arrays.asList(testArray1);
    Collections.shuffle(testList1);
    testList1.toArray(testArray1);

    Contact[] testArray2 = Arrays.copyOf(test2, test2.length);
    List<Contact> testList2 = Arrays.asList(testArray2);
    Collections.shuffle(testList2);
    testList2.toArray(testArray2);

    Sorter.selectionSort(testArray1);
    assertTrue(Arrays.equals(testArray1, test1));

    Sorter.selectionSort(testArray2);
    assertTrue(Arrays.equals(testArray2, test2));
  }

  @Test
  void testInsertion() {
    Contact[] testArray1 = Arrays.copyOf(test1, test1.length);
    List<Contact> testList1 = Arrays.asList(testArray1);
    Collections.shuffle(testList1);
    testList1.toArray(testArray1);

    Contact[] testArray2 = Arrays.copyOf(test2, test2.length);
    List<Contact> testList2 = Arrays.asList(testArray2);
    Collections.shuffle(testList2);
    testList2.toArray(testArray2);

    Sorter.insertionSort(testArray1);
    assertTrue(Arrays.equals(testArray1, test1));

    Sorter.insertionSort(testArray2);
    assertTrue(Arrays.equals(testArray2, test2));
  }

  @Test
  void testQuick() {
    Contact[] testArray1 = Arrays.copyOf(test1, test1.length);
    List<Contact> testList1 = Arrays.asList(testArray1);
    Collections.shuffle(testList1);
    testList1.toArray(testArray1);

    Contact[] testArray2 = Arrays.copyOf(test2, test2.length);
    List<Contact> testList2 = Arrays.asList(testArray2);
    Collections.shuffle(testList2);
    testList2.toArray(testArray2);

    Sorter.quickSort(testArray1);
    assertTrue(Arrays.equals(testArray1, test1));

    Sorter.quickSort(testArray2);
    assertTrue(Arrays.equals(testArray2, test2));
  }

  @Test
  void testMerge() {
    Contact[] testArray1 = Arrays.copyOf(test1, test1.length);
    List<Contact> testList1 = Arrays.asList(testArray1);
    Collections.shuffle(testList1);
    testList1.toArray(testArray1);

    Contact[] testArray2 = Arrays.copyOf(test2, test2.length);
    List<Contact> testList2 = Arrays.asList(testArray2);
    Collections.shuffle(testList2);
    testList2.toArray(testArray2);

    Sorter.mergeSort(testArray1);
    assertTrue(Arrays.equals(testArray1, test1));

    Sorter.mergeSort(testArray2);
    assertTrue(Arrays.equals(testArray2, test2));
  }
}


