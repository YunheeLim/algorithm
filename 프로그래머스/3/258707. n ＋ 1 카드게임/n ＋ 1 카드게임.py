def solution(coin, cards):
    answer = 0
    TARGET = len(cards) + 1
    
    # 손에 있는 카드와, 구매 가능한 카드를 저장하는 리스트
    # IDEA! 버려져 있는 카드도 구매 가능하다.
    onhand = cards[:len(cards)//3]
    canbuy = []
    
    idx = len(onhand)-2
    alive = True
    
    while alive and len(onhand) > 0:
        idx += 2
        answer += 1
        canbuy.extend(cards[idx:idx+2]) # 버린 것도 살 수 있고, 새로 뽑은 것도 살 수 있으므로 일단 버린다.
        alive = False
        
        # Case 1. 일단 내 손에 있는 것만으로 내고 넘어갈 수 있으면 넘어가기
        for card in onhand: 
            if (TARGET-card) in onhand:
                onhand.remove(card)
                onhand.remove(TARGET-card)
                alive = True
                break
        if alive:
            continue
        
        # Case 2. 내 손에 있는 것 한장 + 살 수 있는 것 중에 한장 사서 넘어가기
        if coin < 1:
            break
        for card in onhand:
            if (TARGET - card) in canbuy:
                onhand.remove(card)
                canbuy.remove(TARGET - card)
                coin -= 1
                alive = True
                break
        if alive:
            continue
            
        # Case 3. 살 수 있는 것 중에 두 장 사서 넘어가기
        if coin < 2:
            break  
        for card in canbuy:
            if (TARGET - card) in canbuy:
                canbuy.remove(card)
                canbuy.remove(TARGET-card)
                coin -= 2
                alive = True
                break
    
    # while 반복 조건 중 alive가 아니라 손에 있는 카드를 다 소진한 케이스에 걸린 경우 처리
    if alive:
        answer += 1
        
    return answer
