import Foundation

func solution(_ d:[Int], _ budget:Int) -> Int {
    var check: Int=0
    let ds=d.sorted()//정렬 쓰는게 빠를 것 같아서.
    var cnt=0
    for i in ds{
        check+=i//먼저 값을 더해주고
        if check<=budget{
            cnt+=1//만약에 안넘었으면 갯수 추가, 오버하게 되면 추가안되게 됨
        }
        else{
            break //이건 나머지 경우
        }
        
    }
    return cnt// 갯수 리턴해주기
}
