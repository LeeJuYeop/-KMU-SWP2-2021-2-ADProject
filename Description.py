description = {
    'bubbleSort': "이름 : 버블정렬\n"
                  "시간복잡도 : O(n^2)\n"
                  "설명 : (오름차순 기준)\n"
                  "대표적인 정렬 알고리즘으로, 두 값을 비교하여 큰 값을 뒤로 이동시키는 방식의 정렬이다.\n"
                  "첫 시행에 n번 반복하며, 이후 시행 횟수만큼 반복 횟수를 줄여 불필요한 반복을 제거한다.",
    'bogoSort' : "보고 정렬은 배열이 정렬될 때까지 배열을 무작위로 섞고 확인하기를 반복하는 알고리즘입니다. 평균 시간복잡도는 O(nxn!)이고 최악의 경우에는 O(∞)입니다. 확률에 의존하는 알고리즘으로 운이 좋다면 가장 빠르게 정렬을 완료할 수 있지만 배열의 크기가 커질수록 정렬을 완료할 확률이 극히 낮아지므로 매우 오랜 시간이 걸리는 비효율적인 알고리즘입니다.",
    'cocktailSort' : "칵테일 정렬은 버블정렬의 파생형으로 홀수 번째는 버블 정렬과 동일하게 배열의 앞부터 훑지만 짝수 번째는 배열의 뒤부터 훑으면서 정렬합니다. 시간복잡도는 버블정렬과 마찬가지로 O(n^2)입니다. 배열의 양 끝이 번갈아가면서 정렬되고 중간이 가장 나중에 정렬됩니다. 이 모습이 마치 칵테일을 마구 흔들어 섞는 것처럼 보인다고 하여 칵테일 또는 셰이커 정렬이라고 부릅니다.",
    'countingSort':"계수 정렬은 배열에서 원소가 등장한 횟수를 이용해서 정렬할 위치를 찾는 알고리즘입니다. 시간복잡도는 O(n+k) (k는 데이터의 최댓값을 의미)입니다. 예를 들어 배열이 input = [ 5, 1, 5, 6, 4 ] 면 등장 횟수는 5는 두 번, 4와 1과 6은 한 번이 됩니다. 그리고 각 원소에 대하여 해당 원소의 등장횟수와 해당 원소보다 작은 원소들의 등장횟수를 모두 더한 값을 대응시킵니다. 1은 1, 4는 2, 5는 4, 6은 5가 됩니다. 이 때 이 누적 합이 배열에서 원소가 위치를 나타냅니다. 각각의 누적합을 t라고 할 때 t-1이 원소가 위치할 가장 끝자리입니다. 1은 0번째, 4는 1번째, 5는 3번째, 6은 4번째가 위치하는 가장 끝자리입니다. [ 1, 4, 5, 5, 6 ]",
    'selectionSort':"선택 정렬은 배열을 끝까지 훑으면서 가장 작은 값을 찾아 왼쪽에 정렬시키는 과정을 반복하는 알고리즘입니다. 시간복잡도는 O(n^2)입니다. 예를 들어 첫 번째 시도에서는 배열의 가장 처음부터 끝까지 훑으면서 가장 작은 값을 배열의 가장 첫 번째에 위치시키고 두 번째 시도에서는 배열의 두 번째부터 훑으면서 가장 작은 값을 배열의 두 번째에 위치시킵니다.",
    'introSort':"인트로 정렬은 퀵 정렬, 힙 정렬, 삽입 정렬을 합친 하이브리드 알고리즘입니다. 기본적으로 퀵 정렬로 시작해서 재귀 깊이가 깊어지면 힙 정렬을 사용합니다. 또 효율에 따라서 중간에 삽입정렬을 사용합니다. ",
    'insertSort':"1",
    'heapSort':"2",
    'quickSort':"3"
}
"""
Insertion Sort ( 삽입 정렬 )
삽입 정렬은 k번째 원소를 1부터 k-1까지와 비교해 적절한 위치에 끼워 넣고 그 뒤의 자료를 한 칸씩 뒤로 밀어내는 과정을 반복하는 알고리즘입니다. 시간복잡도는 O(n²)입니다.

Quick Sort ( 퀵 정렬 )
퀵 정렬은 적절한 값(pivot)을 선정하여 그보다 작은 값은 왼쪽으로, 큰 값은 오른쪽으로 옮겨 pivot보다 작은 영역과 큰 영역으로 나눈 뒤 나누어진 각각에서 다시 피벗을 잡고 정렬하는 과정을 반복하는 알고리즘입니다. 시간복잡도는 O(n log n)입니다. pivot값을 선정하는 방법에는 여러 가지가 있으나 우리 프로그램에서는 리스트의 가운데에 위치하는 원소를 pivot으로 선정하도록 만들었습니다.

Heap Sort ( 힙 정렬 )
힙 정렬이란 힙 트리(Heap Tree)개념을 이용하여 정렬을 수행하는 알고리즘입니다. 시간복잡도는 O(n log n)입니다. 힙 트리란 자료구조의 하나로 완전 이진트리의 형태를 가지면서 부모의 값은 항상 자식들의 값보다 크거나(Max heap, 최대 힙), 작아야(Min heap, 최소 힙)작아야 하는 규칙을 따르는 이진트리입니다. 힙 트리 자체는 여러 개의 값 중에서 가장 크거나 작은 값을 빠르게 찾기 위한 용도지만 이 점을 이용해서 가장 큰 값 혹은 가장 작은 값을 계속 골라내면서 정렬하는 것이 가능합니다. 힙 트리 개념을 이해해야 알고리즘을 정확히 이해하는 것이 가능합니다.
"""
