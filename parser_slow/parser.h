#ifndef PARSER_H_
#define PARSER_H_

#include <memory>

class Regex {
public:
    static bool match(const char* s, const std::shared_ptr<Regex>& reg);
    virtual ~Regex() = default;
};

class Char: public Regex {
private:
    char value;

public:
    explicit Char(char value);

    bool operator==(const Char&) const;
};


class Epsilon: public Regex {
public:
    Epsilon() = default;
};

class Empty: public Regex {
public:
    Empty() = default;
};

class Star: public Regex{
private:
    std::shared_ptr<Regex> inside;
public:
    explicit Star(Regex* inside);

    explicit Star(const std::shared_ptr<Regex>& inside);

    std::shared_ptr<Regex> get_inside() const;
};

class BinaryOperator: public Regex {
protected:
    std::shared_ptr<Regex> left, right;
    
public:
    explicit BinaryOperator(Regex* left,  Regex* right);
    explicit BinaryOperator(const std::shared_ptr<Regex>& left, const std::shared_ptr<Regex>& right);

    std::shared_ptr<Regex> get_left() const;
    std::shared_ptr<Regex> get_right() const;
};

class Alt: public BinaryOperator {
public:
    explicit Alt(Regex* left,  Regex* right);
    explicit Alt(const std::shared_ptr<Regex>& left, const std::shared_ptr<Regex>& right);
};

class Concat: public BinaryOperator {
public:
    explicit Concat(Regex* left,  Regex* right);
    explicit Concat(const std::shared_ptr<Regex>& left, const std::shared_ptr<Regex>& right);
};

#endif