


data %>% 
    select(
      "ano",
      grep("c1", names(.)), 
      grep("c2", names(.)), 
      grep("c3", names(.)), 
      grep("c4", names(.))
    ) %>%
    pivot_longer(-ano) %>% 
    group_by(ano, name) %>% 
    summarise(soma=sum(value), maxx=max(value)) %>% 
    pivot_wider(names_from = name, values_from = c("soma", "maxx")) %>% 
    glimpse()