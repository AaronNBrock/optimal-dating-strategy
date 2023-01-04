# An Optimal Dating Strategy

## Introduction
Love is complicated. But… so is the weather, and somehow we manage to predict it (albeit with varying degrees of accuracy).  One might postulate, even if only as a thought experiment, what is the optimal strategy for dating such that one is guaranteed the best possible spouse?  Now, before we can start down this path, we must first define the axioms of the problem space.  The dating equivalent of Physic's “Assume a massless frictionless object”.   As well as clearly defining what we're optimizing for, so we have a way of measuring success.

There are also many aspects of dating, such as how to find potential partners, how to attract such partners, once in a relationship how to optimize it for one's happiness, etc.  All of which, I believe, are interesting problems in their own right.  But, for the purposes of this post, I want to focus on the issue of selection.  With this in mind, the problem statement I've come up with is:

> Given N number of penitential mates in one's life, what is the optimal strategy for selecting a mate such that you end up with the best possible partner.

To make this problem more manageable, I've come up with the following axioms.  However, I encourage considering the ramifications of what a solution would like given different axioms:

* Every relationship can be summed up to a single value, which we'll call one's “compatibility”.
* You can only be in one relationship at a time.
* Once one passes on a relationship, there is no going back.
* We can estimate how many potential relationships one could have in their life (again, not solving the problem of finding partners here).
* It is solely your choice as to if you would like to marry your current partner.

Of course these are not an exact representation of the complexities of life, but it's a starting point that allows us to design a simulation, so we can test different algorithms.

## The Naive Algorithm
Now, with all that out of the way.  Let's get a baseline of performance.  The simplest algorithm one could imagine is to opt to marry the first person they date.  Since I'm an engineer and not a mathematician, I wrote a program to simulate this (which you can find on my GitHub).  As a quick aside, for the purposes of that program, all partners will be uniformly generated between 0 and 100. However, it should be noted that one should not assume that will be the case in the real world, in fact, I would love if someone could provide information as to what the actual distribution might be.

In any event, the programmatic version of this simple algorithm would look like:

```python
def dating_strategy(
    past_partners,
    current_partner,
    number_of_potential_partners
):
    return True
```

And, unsurprisingly, this results in an average spouse value of the average of all potential partners, in my programs' case that's 50.  But can we do better?

If you would like to try out this problem by yourself, please do so now before reading the next paragraph that's coming in 3… 2… 1…

## The Optimal Algorithm
While I am not a mathematician, my dear father _is_, and after a father-son conversation about what the optimal algorithm for a dating strategy might be, you know normal father-son stuff.  I learned that, amazingly, this is actually a solved problem.  In their paper “Recognizing the maximum of a sequence” John P. Gilbert and Frederick Mosteller call the problem the beauty contest problem, the secretary problem, Googol, or the dowry problem. They say, “Our efforts to discover the originator of this problem have been unsuccessful.”  But, to succinctly explain the actual algorithm, the idea is you skip the first 1/e number of partners then marry the first one, which is better than anyone you've seen so far.  Or, written in code it looks like:

```python
def dating_strategy(
    past_partners,
    current_partner,
    number_of_potential_partners
):
    return (
        len(past_partners) > (number_of_potential_partners / math.e) and
        current_partner > max(past_partners)
    )
```

This algorithm has an average spouse value of ~86.2, which is the best possible performance.  It is unfortunately above my pay grade to prove why, but if you're curious, I suggest [the book referenced earlier](https://books.google.com/books?id=dcgUsrsaZRYC).

This algorithm does have some interesting properties, for example ~37% of the time the optimal partner will be skipped in the beginning whilst in the “collecting data” phase.  Leading to, by necessity, being forced to marry whoever happens to be last.  Or, in the real-world, one might not know which one is last and end up unmarried.

## How to apply this to life?
Now, before blindly skipping on your high school sweetheart because they fall in the first 36.788% of potential partners and, well, that's just not optimal.  I would suggest remembering that this model we built had axioms which may not be representative of real life and doesn't account for things like:

* How people's compatibility changes over time
* We don't truly know your number of potential partners
* There is, in fact, no rule disallowing you from dating an ex (Something I've unfortunately done before…)
* etc.

But I, personally, find this a useful thought experiment which helps inform my decisions and relieve stress levels as they relate to my romantic life.  For example, in my life, I've made the rough estimate that I could realistically have about 10 partners in my life.  And that since I have dated 3 people so far, it stands to reason that I intend to marry the next person I date who, I believe, is better than all those who've come before.

## Conclusion
The thought of how to optimize dating has been on my mind lately.  While currently I'm focusing my efforts on ensuring a successful career, looking at the trends in my life I believe that romantic entanglement will soon be a higher priority.  And, I would like to have a clear strategy once focusing on it.  I see thought experiments like this as an avenue to achieve that.  Publishing helps me get feedback on my strategy to refine it (as well as being an avenue to potentially attract partners of a similar mindset… since, I know you'll be shocked to hear, I'm single right now).  So, I encourage you to leave feedback to help myself and others interested in this problem space.

Furthermore, I'd like to explicitly state that I appreciate you taking the time to read this blog.  If you found it intriguing, it would be wondrous if you could share it with someone you think might appreciate this approach to partner selection!

