from __clrclasses__.System import Comparison as _n_0_t_0
from __clrclasses__.System import ValueType as _n_0_t_1
from __clrclasses__.System import Predicate as _n_0_t_2
from __clrclasses__.System import Array as _n_0_t_3
from __clrclasses__.System import IDisposable as _n_0_t_4
from __clrclasses__.System import SystemException as _n_0_t_5
from __clrclasses__.System import Exception as _n_0_t_6
from __clrclasses__.System import Converter as _n_0_t_7
from __clrclasses__.System import Action as _n_0_t_8
from __clrclasses__.System import Func as _n_0_t_9
from __clrclasses__.System.Collections import IComparer as _n_1_t_0
from __clrclasses__.System.Collections import IDictionary as _n_1_t_1
from __clrclasses__.System.Collections import IDictionaryEnumerator as _n_1_t_2
from __clrclasses__.System.Collections import ICollection as _n_1_t_3
from __clrclasses__.System.Collections import IEqualityComparer as _n_1_t_4
from __clrclasses__.System.Collections import IEnumerable as _n_1_t_5
from __clrclasses__.System.Collections import IEnumerator as _n_1_t_6
from __clrclasses__.System.Collections import IList as _n_1_t_7
from __clrclasses__.System.Collections.ObjectModel import ReadOnlyCollection as _n_2_t_0
from __clrclasses__.System.Linq import ParallelQuery as _n_3_t_0
from __clrclasses__.System.Linq import IQueryable as _n_3_t_1
from __clrclasses__.System.Linq import IGrouping as _n_3_t_2
from __clrclasses__.System.Linq import IOrderedEnumerable as _n_3_t_3
from __clrclasses__.System.Linq import ILookup as _n_3_t_4
from __clrclasses__.System.Runtime.InteropServices import _Exception as _n_4_t_0
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_5_t_0
from __clrclasses__.System.Runtime.Serialization import IDeserializationCallback as _n_5_t_1
import typing
T = typing.TypeVar('T')
TKey = typing.TypeVar('TKey')
TValue = typing.TypeVar('TValue')
class Comparer(_n_1_t_0, IComparer[T], typing.Generic[T]):
    @property
    def Default(self) -> Comparer[T]:"""Default { get; } -> Comparer"""
    @staticmethod
    def Create(comparison: _n_0_t_0[T]) -> Comparer[T]:...
class Dictionary(IDictionary[TKey, TValue], _n_1_t_1, IReadOnlyDictionary[TKey, TValue], _n_5_t_0, _n_5_t_1, typing.Generic[TKey, TValue], typing.Iterable[TValue]):
    @property
    def Comparer(self) -> IEqualityComparer[TKey]:"""Comparer { get; } -> IEqualityComparer"""
    def __init__(self, dictionary: IDictionary[TKey, TValue]) -> Dictionary:...
    def __init__(self, dictionary: IDictionary[TKey, TValue], comparer: IEqualityComparer[TKey]) -> Dictionary:...
    def __init__(self, capacity: int, comparer: IEqualityComparer[TKey]) -> Dictionary:...
    def __init__(self, comparer: IEqualityComparer[TKey]) -> Dictionary:...
    def __init__(self, capacity: int) -> Dictionary:...
    def __init__(self) -> Dictionary:...
    def ContainsValue(self, value: TValue) -> bool:...
    class Enumerator(_n_0_t_1, IEnumerator[KeyValuePair[TKey, TValue]], _n_1_t_2, typing.Generic[TKey, TValue]):
        pass
    class KeyCollection(ICollection[TKey], _n_1_t_3, IReadOnlyCollection[TKey], typing.Generic[TKey, TValue]):
        def __init__(self, dictionary: Dictionary[TKey, TValue]) -> Dictionary.KeyCollection:...
        class Enumerator(_n_0_t_1, IEnumerator[TKey], typing.Generic[TKey, TValue]):
            pass
    class ValueCollection(ICollection[TValue], _n_1_t_3, IReadOnlyCollection[TValue], typing.Generic[TKey, TValue]):
        def __init__(self, dictionary: Dictionary[TKey, TValue]) -> Dictionary.ValueCollection:...
        class Enumerator(_n_0_t_1, IEnumerator[TValue], typing.Generic[TKey, TValue]):
            pass
class EqualityComparer(_n_1_t_4, IEqualityComparer[T], typing.Generic[T]):
    @property
    def Default(self) -> EqualityComparer[T]:"""Default { get; } -> EqualityComparer"""
class HashSet(ICollection[T], _n_5_t_0, _n_5_t_1, ISet[T], IReadOnlyCollection[T], typing.Generic[T]):
    @property
    def Comparer(self) -> IEqualityComparer[T]:"""Comparer { get; } -> IEqualityComparer"""
    def __init__(self) -> HashSet:...
    def __init__(self, comparer: IEqualityComparer[T]) -> HashSet:...
    def __init__(self, collection: IEnumerable[T]) -> HashSet:...
    def __init__(self, collection: IEnumerable[T], comparer: IEqualityComparer[T]) -> HashSet:...
    def __init__(self, capacity: int) -> HashSet:...
    def __init__(self, capacity: int, comparer: IEqualityComparer[T]) -> HashSet:...
    @staticmethod
    def CreateSetComparer() -> IEqualityComparer[HashSet[T]]:...
    def RemoveWhere(self, match: _n_0_t_2[T]) -> int:...
    def TrimExcess(self):...
    def TryGetValue(self, equalValue: T, actualValue: object) -> bool:...
    class Enumerator(_n_0_t_1, IEnumerator[T], typing.Generic[T]):
        pass
class ICollection(IEnumerable[T], typing.Generic[T]):
    @property
    def Count(self) -> int:"""Count { get; } -> int"""
    @property
    def IsReadOnly(self) -> bool:"""IsReadOnly { get; } -> bool"""
    def Add(self, item: T):...
    def Clear(self):...
    def Contains(self, item: T) -> bool:...
    def CopyTo(self, array: _n_0_t_3[T], arrayIndex: int):...
    def Remove(self, item: T) -> bool:...
class IComparer(typing.Generic[T]):
    def Compare(self, x: T, y: T) -> int:...
class IDictionary(ICollection[KeyValuePair[TKey, TValue]], typing.Generic[TKey, TValue], typing.Iterable[TValue]):
    @property
    def Item(self) -> TValue:"""Item { get; set; } -> TValue"""
    @property
    def Keys(self) -> ICollection[TKey]:"""Keys { get; } -> ICollection"""
    @property
    def Values(self) -> ICollection[TValue]:"""Values { get; } -> ICollection"""
    def ContainsKey(self, key: TKey) -> bool:...
    def TryGetValue(self, key: TKey, value: object) -> bool:...
class IEnumerable(_n_1_t_5, typing.Generic[T]):
    def Aggregate(self, func: _n_0_t_9[typing.Any, typing.Any, typing.Any]) -> typing.Any:
        """Extension from: System.Linq.Enumerable"""
    def Aggregate(self, seed: typing.Any, func: _n_0_t_9[typing.Any, typing.Any, typing.Any]) -> typing.Any:
        """Extension from: System.Linq.Enumerable"""
    def Aggregate(self, seed: typing.Any, func: _n_0_t_9[typing.Any, typing.Any, typing.Any], resultSelector: _n_0_t_9[typing.Any, typing.Any]) -> typing.Any:
        """Extension from: System.Linq.Enumerable"""
    def All(self, predicate: _n_0_t_9[typing.Any, bool]) -> bool:
        """Extension from: System.Linq.Enumerable"""
    def Any(self) -> bool:
        """Extension from: System.Linq.Enumerable"""
    def Any(self, predicate: _n_0_t_9[typing.Any, bool]) -> bool:
        """Extension from: System.Linq.Enumerable"""
    def Append(self, element: typing.Any) -> IEnumerable[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def AsEnumerable(self) -> IEnumerable[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def AsParallel(self) -> _n_3_t_0[typing.Any]:
        """Extension from: System.Linq.ParallelEnumerable"""
    def AsQueryable(self) -> _n_3_t_1[typing.Any]:
        """Extension from: System.Linq.Queryable"""
    def Average(self) -> float:
        """Extension from: System.Linq.Enumerable"""
    def Average(self, selector: _n_0_t_9[typing.Any, int]) -> float:
        """Extension from: System.Linq.Enumerable"""
    def Concat(self, second: IEnumerable[typing.Any]) -> IEnumerable[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def Contains(self, value: typing.Any) -> bool:
        """Extension from: System.Linq.Enumerable"""
    def Contains(self, value: typing.Any, comparer: IEqualityComparer[typing.Any]) -> bool:
        """Extension from: System.Linq.Enumerable"""
    def Count(self) -> int:
        """Extension from: System.Linq.Enumerable"""
    def Count(self, predicate: _n_0_t_9[typing.Any, bool]) -> int:
        """Extension from: System.Linq.Enumerable"""
    def DefaultIfEmpty(self) -> IEnumerable[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def DefaultIfEmpty(self, defaultValue: typing.Any) -> IEnumerable[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def Distinct(self) -> IEnumerable[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def Distinct(self, comparer: IEqualityComparer[typing.Any]) -> IEnumerable[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def ElementAt(self, index: int) -> typing.Any:
        """Extension from: System.Linq.Enumerable"""
    def ElementAtOrDefault(self, index: int) -> typing.Any:
        """Extension from: System.Linq.Enumerable"""
    def Except(self, second: IEnumerable[typing.Any]) -> IEnumerable[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def Except(self, second: IEnumerable[typing.Any], comparer: IEqualityComparer[typing.Any]) -> IEnumerable[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def First(self) -> typing.Any:
        """Extension from: System.Linq.Enumerable"""
    def First(self, predicate: _n_0_t_9[typing.Any, bool]) -> typing.Any:
        """Extension from: System.Linq.Enumerable"""
    def FirstOrDefault(self) -> typing.Any:
        """Extension from: System.Linq.Enumerable"""
    def FirstOrDefault(self, predicate: _n_0_t_9[typing.Any, bool]) -> typing.Any:
        """Extension from: System.Linq.Enumerable"""
    def GroupBy(self, keySelector: _n_0_t_9[typing.Any, typing.Any]) -> IEnumerable[_n_3_t_2[typing.Any, typing.Any]]:
        """Extension from: System.Linq.Enumerable"""
    def GroupBy(self, keySelector: _n_0_t_9[typing.Any, typing.Any], comparer: IEqualityComparer[typing.Any]) -> IEnumerable[_n_3_t_2[typing.Any, typing.Any]]:
        """Extension from: System.Linq.Enumerable"""
    def GroupBy(self, keySelector: _n_0_t_9[typing.Any, typing.Any], elementSelector: _n_0_t_9[typing.Any, typing.Any]) -> IEnumerable[_n_3_t_2[typing.Any, typing.Any]]:
        """Extension from: System.Linq.Enumerable"""
    def GroupBy(self, keySelector: _n_0_t_9[typing.Any, typing.Any], elementSelector: _n_0_t_9[typing.Any, typing.Any], comparer: IEqualityComparer[typing.Any]) -> IEnumerable[_n_3_t_2[typing.Any, typing.Any]]:
        """Extension from: System.Linq.Enumerable"""
    def GroupBy(self, keySelector: _n_0_t_9[typing.Any, typing.Any], elementSelector: _n_0_t_9[typing.Any, typing.Any], resultSelector: _n_0_t_9[typing.Any, IEnumerable[typing.Any], typing.Any]) -> IEnumerable[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def GroupBy(self, keySelector: _n_0_t_9[typing.Any, typing.Any], elementSelector: _n_0_t_9[typing.Any, typing.Any], resultSelector: _n_0_t_9[typing.Any, IEnumerable[typing.Any], typing.Any], comparer: IEqualityComparer[typing.Any]) -> IEnumerable[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def GroupJoin(self, inner: IEnumerable[typing.Any], outerKeySelector: _n_0_t_9[typing.Any, typing.Any], innerKeySelector: _n_0_t_9[typing.Any, typing.Any], resultSelector: _n_0_t_9[typing.Any, IEnumerable[typing.Any], typing.Any]) -> IEnumerable[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def GroupJoin(self, inner: IEnumerable[typing.Any], outerKeySelector: _n_0_t_9[typing.Any, typing.Any], innerKeySelector: _n_0_t_9[typing.Any, typing.Any], resultSelector: _n_0_t_9[typing.Any, IEnumerable[typing.Any], typing.Any], comparer: IEqualityComparer[typing.Any]) -> IEnumerable[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def Intersect(self, second: IEnumerable[typing.Any]) -> IEnumerable[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def Intersect(self, second: IEnumerable[typing.Any], comparer: IEqualityComparer[typing.Any]) -> IEnumerable[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def Join(self, inner: IEnumerable[typing.Any], outerKeySelector: _n_0_t_9[typing.Any, typing.Any], innerKeySelector: _n_0_t_9[typing.Any, typing.Any], resultSelector: _n_0_t_9[typing.Any, typing.Any, typing.Any]) -> IEnumerable[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def Join(self, inner: IEnumerable[typing.Any], outerKeySelector: _n_0_t_9[typing.Any, typing.Any], innerKeySelector: _n_0_t_9[typing.Any, typing.Any], resultSelector: _n_0_t_9[typing.Any, typing.Any, typing.Any], comparer: IEqualityComparer[typing.Any]) -> IEnumerable[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def Last(self) -> typing.Any:
        """Extension from: System.Linq.Enumerable"""
    def Last(self, predicate: _n_0_t_9[typing.Any, bool]) -> typing.Any:
        """Extension from: System.Linq.Enumerable"""
    def LastOrDefault(self) -> typing.Any:
        """Extension from: System.Linq.Enumerable"""
    def LastOrDefault(self, predicate: _n_0_t_9[typing.Any, bool]) -> typing.Any:
        """Extension from: System.Linq.Enumerable"""
    def LongCount(self) -> int:
        """Extension from: System.Linq.Enumerable"""
    def LongCount(self, predicate: _n_0_t_9[typing.Any, bool]) -> int:
        """Extension from: System.Linq.Enumerable"""
    def Max(self) -> int:
        """Extension from: System.Linq.Enumerable"""
    def Max(self, selector: _n_0_t_9[typing.Any, int]) -> int:
        """Extension from: System.Linq.Enumerable"""
    def Min(self) -> int:
        """Extension from: System.Linq.Enumerable"""
    def Min(self, selector: _n_0_t_9[typing.Any, int]) -> int:
        """Extension from: System.Linq.Enumerable"""
    def OrderBy(self, keySelector: _n_0_t_9[typing.Any, typing.Any]) -> _n_3_t_3[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def OrderBy(self, keySelector: _n_0_t_9[typing.Any, typing.Any], comparer: IComparer[typing.Any]) -> _n_3_t_3[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def OrderByDescending(self, keySelector: _n_0_t_9[typing.Any, typing.Any]) -> _n_3_t_3[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def OrderByDescending(self, keySelector: _n_0_t_9[typing.Any, typing.Any], comparer: IComparer[typing.Any]) -> _n_3_t_3[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def Prepend(self, element: typing.Any) -> IEnumerable[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def Reverse(self) -> IEnumerable[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def Select(self, selector: _n_0_t_9[typing.Any, typing.Any]) -> IEnumerable[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def SelectMany(self, selector: _n_0_t_9[typing.Any, IEnumerable[typing.Any]]) -> IEnumerable[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def SelectMany(self, collectionSelector: _n_0_t_9[typing.Any, int, IEnumerable[typing.Any]], resultSelector: _n_0_t_9[typing.Any, typing.Any, typing.Any]) -> IEnumerable[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def SequenceEqual(self, second: IEnumerable[typing.Any]) -> bool:
        """Extension from: System.Linq.Enumerable"""
    def SequenceEqual(self, second: IEnumerable[typing.Any], comparer: IEqualityComparer[typing.Any]) -> bool:
        """Extension from: System.Linq.Enumerable"""
    def Single(self) -> typing.Any:
        """Extension from: System.Linq.Enumerable"""
    def Single(self, predicate: _n_0_t_9[typing.Any, bool]) -> typing.Any:
        """Extension from: System.Linq.Enumerable"""
    def SingleOrDefault(self) -> typing.Any:
        """Extension from: System.Linq.Enumerable"""
    def SingleOrDefault(self, predicate: _n_0_t_9[typing.Any, bool]) -> typing.Any:
        """Extension from: System.Linq.Enumerable"""
    def Skip(self, count: int) -> IEnumerable[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def SkipWhile(self, predicate: _n_0_t_9[typing.Any, bool]) -> IEnumerable[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def Sum(self) -> int:
        """Extension from: System.Linq.Enumerable"""
    def Sum(self, selector: _n_0_t_9[typing.Any, int]) -> int:
        """Extension from: System.Linq.Enumerable"""
    def Take(self, count: int) -> IEnumerable[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def TakeWhile(self, predicate: _n_0_t_9[typing.Any, bool]) -> IEnumerable[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def ToArray(self) -> _n_0_t_3[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def ToDictionary(self, keySelector: _n_0_t_9[typing.Any, typing.Any]) -> Dictionary[typing.Any, typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def ToDictionary(self, keySelector: _n_0_t_9[typing.Any, typing.Any], comparer: IEqualityComparer[typing.Any]) -> Dictionary[typing.Any, typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def ToDictionary(self, keySelector: _n_0_t_9[typing.Any, typing.Any], elementSelector: _n_0_t_9[typing.Any, typing.Any]) -> Dictionary[typing.Any, typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def ToDictionary(self, keySelector: _n_0_t_9[typing.Any, typing.Any], elementSelector: _n_0_t_9[typing.Any, typing.Any], comparer: IEqualityComparer[typing.Any]) -> Dictionary[typing.Any, typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def ToHashSet(self) -> HashSet[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def ToHashSet(self, comparer: IEqualityComparer[typing.Any]) -> HashSet[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def ToList(self) -> List[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def ToLookup(self, keySelector: _n_0_t_9[typing.Any, typing.Any]) -> _n_3_t_4[typing.Any, typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def ToLookup(self, keySelector: _n_0_t_9[typing.Any, typing.Any], comparer: IEqualityComparer[typing.Any]) -> _n_3_t_4[typing.Any, typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def ToLookup(self, keySelector: _n_0_t_9[typing.Any, typing.Any], elementSelector: _n_0_t_9[typing.Any, typing.Any]) -> _n_3_t_4[typing.Any, typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def ToLookup(self, keySelector: _n_0_t_9[typing.Any, typing.Any], elementSelector: _n_0_t_9[typing.Any, typing.Any], comparer: IEqualityComparer[typing.Any]) -> _n_3_t_4[typing.Any, typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def Union(self, second: IEnumerable[typing.Any]) -> IEnumerable[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def Union(self, second: IEnumerable[typing.Any], comparer: IEqualityComparer[typing.Any]) -> IEnumerable[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def Where(self, predicate: _n_0_t_9[typing.Any, bool]) -> IEnumerable[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
    def Zip(self, second: IEnumerable[typing.Any], resultSelector: _n_0_t_9[typing.Any, typing.Any, typing.Any]) -> IEnumerable[typing.Any]:
        """Extension from: System.Linq.Enumerable"""
class IEnumerator(_n_0_t_4, _n_1_t_6, typing.Generic[T]):
    pass
class IEqualityComparer(typing.Generic[T]):
    def Equals(self, x: T, y: T) -> bool:...
    def GetHashCode(self, obj: T) -> int:...
class IList(ICollection[T], typing.Generic[T], typing.Iterable[T]):
    @property
    def Item(self) -> T:"""Item { get; set; } -> T"""
    def IndexOf(self, item: T) -> int:...
    def Insert(self, index: int, item: T):...
    def RemoveAt(self, index: int):...
class IReadOnlyCollection(IEnumerable[T], typing.Generic[T]):
    @property
    def Count(self) -> int:"""Count { get; } -> int"""
class IReadOnlyDictionary(IReadOnlyCollection[KeyValuePair[TKey, TValue]], typing.Generic[TKey, TValue], typing.Iterable[TValue]):
    @property
    def Item(self) -> TValue:"""Item { get; } -> TValue"""
    @property
    def Keys(self) -> IEnumerable[TKey]:"""Keys { get; } -> IEnumerable"""
    @property
    def Values(self) -> IEnumerable[TValue]:"""Values { get; } -> IEnumerable"""
    def ContainsKey(self, key: TKey) -> bool:...
    def TryGetValue(self, key: TKey, value: object) -> bool:...
class IReadOnlyList(IReadOnlyCollection[T], typing.Generic[T], typing.Iterable[T]):
    @property
    def Item(self) -> T:"""Item { get; } -> T"""
class ISet(ICollection[T], typing.Generic[T]):
    def ExceptWith(self, other: IEnumerable[T]):...
    def IntersectWith(self, other: IEnumerable[T]):...
    def IsProperSubsetOf(self, other: IEnumerable[T]) -> bool:...
    def IsProperSupersetOf(self, other: IEnumerable[T]) -> bool:...
    def IsSubsetOf(self, other: IEnumerable[T]) -> bool:...
    def IsSupersetOf(self, other: IEnumerable[T]) -> bool:...
    def Overlaps(self, other: IEnumerable[T]) -> bool:...
    def SetEquals(self, other: IEnumerable[T]) -> bool:...
    def SymmetricExceptWith(self, other: IEnumerable[T]):...
    def UnionWith(self, other: IEnumerable[T]):...
class KeyNotFoundException(_n_0_t_5, _n_5_t_0, _n_4_t_0):
    def __init__(self, message: str, innerException: _n_0_t_6) -> KeyNotFoundException:...
    def __init__(self, message: str) -> KeyNotFoundException:...
    def __init__(self) -> KeyNotFoundException:...
class KeyValuePair(_n_0_t_1, typing.Generic[TKey, TValue]):
    @property
    def Key(self) -> TKey:"""Key { get; } -> TKey"""
    @property
    def Value(self) -> TValue:"""Value { get; } -> TValue"""
    def __init__(self, key: TKey, value: TValue) -> KeyValuePair:...
class LinkedList(ICollection[T], _n_1_t_3, IReadOnlyCollection[T], _n_5_t_0, _n_5_t_1, typing.Generic[T]):
    @property
    def First(self) -> LinkedListNode[T]:"""First { get; } -> LinkedListNode"""
    @property
    def Last(self) -> LinkedListNode[T]:"""Last { get; } -> LinkedListNode"""
    def __init__(self, collection: IEnumerable[T]) -> LinkedList:...
    def __init__(self) -> LinkedList:...
    def AddAfter(self, node: LinkedListNode[T], value: T) -> LinkedListNode[T]:...
    def AddAfter(self, node: LinkedListNode[T], newNode: LinkedListNode[T]):...
    def AddBefore(self, node: LinkedListNode[T], newNode: LinkedListNode[T]):...
    def AddBefore(self, node: LinkedListNode[T], value: T) -> LinkedListNode[T]:...
    def AddFirst(self, node: LinkedListNode[T]):...
    def AddFirst(self, value: T) -> LinkedListNode[T]:...
    def AddLast(self, node: LinkedListNode[T]):...
    def AddLast(self, value: T) -> LinkedListNode[T]:...
    def Find(self, value: T) -> LinkedListNode[T]:...
    def FindLast(self, value: T) -> LinkedListNode[T]:...
    def RemoveFirst(self):...
    def RemoveLast(self):...
    class Enumerator(_n_0_t_1, IEnumerator[T], _n_5_t_0, _n_5_t_1, typing.Generic[T]):
        pass
class LinkedListNode(typing.Generic[T]):
    @property
    def List(self) -> LinkedList[T]:"""List { get; } -> LinkedList"""
    @property
    def Next(self) -> LinkedListNode[T]:"""Next { get; } -> LinkedListNode"""
    @property
    def Previous(self) -> LinkedListNode[T]:"""Previous { get; } -> LinkedListNode"""
    @property
    def Value(self) -> T:"""Value { get; set; } -> T"""
    def __init__(self, value: T) -> LinkedListNode:...
class List(IList[T], _n_1_t_7, IReadOnlyList[T], typing.Generic[T], typing.Iterable[T]):
    @property
    def Capacity(self) -> int:"""Capacity { get; set; } -> int"""
    def __init__(self, collection: IEnumerable[T]) -> List:...
    def __init__(self, capacity: int) -> List:...
    def __init__(self) -> List:...
    def AddRange(self, collection: IEnumerable[T]):...
    def AsReadOnly(self) -> _n_2_t_0[T]:...
    def BinarySearch(self, item: T, comparer: IComparer[T]) -> int:...
    def BinarySearch(self, item: T) -> int:...
    def BinarySearch(self, index: int, count: int, item: T, comparer: IComparer[T]) -> int:...
    def ConvertAll(self, converter: _n_0_t_7[T, typing.Any]) -> List[typing.Any]:...
    def Exists(self, match: _n_0_t_2[T]) -> bool:...
    def Find(self, match: _n_0_t_2[T]) -> T:...
    def FindAll(self, match: _n_0_t_2[T]) -> List[T]:...
    def FindIndex(self, startIndex: int, count: int, match: _n_0_t_2[T]) -> int:...
    def FindIndex(self, startIndex: int, match: _n_0_t_2[T]) -> int:...
    def FindIndex(self, match: _n_0_t_2[T]) -> int:...
    def FindLast(self, match: _n_0_t_2[T]) -> T:...
    def FindLastIndex(self, startIndex: int, count: int, match: _n_0_t_2[T]) -> int:...
    def FindLastIndex(self, startIndex: int, match: _n_0_t_2[T]) -> int:...
    def FindLastIndex(self, match: _n_0_t_2[T]) -> int:...
    def ForEach(self, action: _n_0_t_8[T]):...
    def GetRange(self, index: int, count: int) -> List[T]:...
    def InsertRange(self, index: int, collection: IEnumerable[T]):...
    def LastIndexOf(self, item: T, index: int, count: int) -> int:...
    def LastIndexOf(self, item: T, index: int) -> int:...
    def LastIndexOf(self, item: T) -> int:...
    def RemoveAll(self, match: _n_0_t_2[T]) -> int:...
    def RemoveRange(self, index: int, count: int):...
    def Reverse(self):...
    def Reverse(self, index: int, count: int):...
    def Sort(self, comparison: _n_0_t_0[T]):...
    def Sort(self, index: int, count: int, comparer: IComparer[T]):...
    def Sort(self, comparer: IComparer[T]):...
    def Sort(self):...
    def ToArray(self) -> _n_0_t_3[T]:...
    def TrimExcess(self):...
    def TrueForAll(self, match: _n_0_t_2[T]) -> bool:...
    class Enumerator(_n_0_t_1, IEnumerator[T], typing.Generic[T]):
        pass
class Queue(IEnumerable[T], _n_1_t_3, IReadOnlyCollection[T], typing.Generic[T]):
    def __init__(self, collection: IEnumerable[T]) -> Queue:...
    def __init__(self, capacity: int) -> Queue:...
    def __init__(self) -> Queue:...
    def Clear(self):...
    def Contains(self, item: T) -> bool:...
    def Dequeue(self) -> T:...
    def Enqueue(self, item: T):...
    def Peek(self) -> T:...
    def ToArray(self) -> _n_0_t_3[T]:...
    def TrimExcess(self):...
    class Enumerator(_n_0_t_1, IEnumerator[T], typing.Generic[T]):
        pass
class SortedDictionary(IDictionary[TKey, TValue], _n_1_t_1, IReadOnlyDictionary[TKey, TValue], typing.Generic[TKey, TValue], typing.Iterable[TValue]):
    @property
    def Comparer(self) -> IComparer[TKey]:"""Comparer { get; } -> IComparer"""
    def __init__(self, dictionary: IDictionary[TKey, TValue], comparer: IComparer[TKey]) -> SortedDictionary:...
    def __init__(self, dictionary: IDictionary[TKey, TValue]) -> SortedDictionary:...
    def __init__(self, comparer: IComparer[TKey]) -> SortedDictionary:...
    def __init__(self) -> SortedDictionary:...
    def ContainsValue(self, value: TValue) -> bool:...
    class Enumerator(_n_0_t_1, IEnumerator[KeyValuePair[TKey, TValue]], _n_1_t_2, typing.Generic[TKey, TValue]):
        pass
    class KeyCollection(ICollection[TKey], _n_1_t_3, IReadOnlyCollection[TKey], typing.Generic[TKey, TValue]):
        def __init__(self, dictionary: SortedDictionary[TKey, TValue]) -> SortedDictionary.KeyCollection:...
        class Enumerator(_n_0_t_1, IEnumerator[TKey], typing.Generic[TKey, TValue]):
            pass
    class ValueCollection(ICollection[TValue], _n_1_t_3, IReadOnlyCollection[TValue], typing.Generic[TKey, TValue]):
        def __init__(self, dictionary: SortedDictionary[TKey, TValue]) -> SortedDictionary.ValueCollection:...
        class Enumerator(_n_0_t_1, IEnumerator[TValue], typing.Generic[TKey, TValue]):
            pass
class SortedList(IDictionary[TKey, TValue], _n_1_t_1, IReadOnlyDictionary[TKey, TValue], typing.Generic[TKey, TValue], typing.Iterable[TValue]):
    @property
    def Capacity(self) -> int:"""Capacity { get; set; } -> int"""
    @property
    def Comparer(self) -> IComparer[TKey]:"""Comparer { get; } -> IComparer"""
    def __init__(self, dictionary: IDictionary[TKey, TValue], comparer: IComparer[TKey]) -> SortedList:...
    def __init__(self, dictionary: IDictionary[TKey, TValue]) -> SortedList:...
    def __init__(self, capacity: int, comparer: IComparer[TKey]) -> SortedList:...
    def __init__(self, comparer: IComparer[TKey]) -> SortedList:...
    def __init__(self, capacity: int) -> SortedList:...
    def __init__(self) -> SortedList:...
    def ContainsValue(self, value: TValue) -> bool:...
    def IndexOfKey(self, key: TKey) -> int:...
    def IndexOfValue(self, value: TValue) -> int:...
    def RemoveAt(self, index: int):...
    def TrimExcess(self):...
class SortedSet(ISet[T], _n_1_t_3, _n_5_t_0, _n_5_t_1, IReadOnlyCollection[T], typing.Generic[T]):
    @property
    def Comparer(self) -> IComparer[T]:"""Comparer { get; } -> IComparer"""
    @property
    def Max(self) -> T:"""Max { get; } -> T"""
    @property
    def Min(self) -> T:"""Min { get; } -> T"""
    def __init__(self, comparer: IComparer[T]) -> SortedSet:...
    def __init__(self, collection: IEnumerable[T], comparer: IComparer[T]) -> SortedSet:...
    def __init__(self, collection: IEnumerable[T]) -> SortedSet:...
    def __init__(self) -> SortedSet:...
    @staticmethod
    def CreateSetComparer(memberEqualityComparer: IEqualityComparer[T]) -> IEqualityComparer[SortedSet[T]]:...
    @staticmethod
    def CreateSetComparer() -> IEqualityComparer[SortedSet[T]]:...
    def GetViewBetween(self, lowerValue: T, upperValue: T) -> SortedSet[T]:...
    def RemoveWhere(self, match: _n_0_t_2[T]) -> int:...
    def Reverse(self) -> IEnumerable[T]:...
    def TryGetValue(self, equalValue: T, actualValue: object) -> bool:...
    class Enumerator(_n_0_t_1, IEnumerator[T], _n_5_t_0, _n_5_t_1, typing.Generic[T]):
        pass
class Stack(IEnumerable[T], _n_1_t_3, IReadOnlyCollection[T], typing.Generic[T]):
    def __init__(self, collection: IEnumerable[T]) -> Stack:...
    def __init__(self, capacity: int) -> Stack:...
    def __init__(self) -> Stack:...
    def Clear(self):...
    def Contains(self, item: T) -> bool:...
    def Peek(self) -> T:...
    def Pop(self) -> T:...
    def Push(self, item: T):...
    def ToArray(self) -> _n_0_t_3[T]:...
    def TrimExcess(self):...
    class Enumerator(_n_0_t_1, IEnumerator[T], typing.Generic[T]):
        pass
